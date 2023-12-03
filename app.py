from flask import Flask, request
from db import db
import email_automater
import json
db_filename = "culturecare.db"
app = Flask(__name__)
import dao
import os
import dotenv
dotenv.load_dotenv()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.drop_all()
    db.create_all()

def assert_none(data):

    for content in data:
        if content is None:
            return True
    return False

def success_response(data, code = 200):
    """
    Generalized success response function
    """
    return json.dumps(data), code

def failure_response(data, code = 404):
    """
    Generalized failure response function
    """
    return json.dumps({"error" : data}), code

def get_automatic_email_response():
    """
    Retrieves and returns pre-written email response written by practitioner
    """


def send_automatic_email_response():
    """
    Sends pre-written email response written by practitioner to patient
    """


@app.route("/emails/prewritten/create/", methods = ["POST"])
def create_prewritten_email():
    """
    Endpoint to create prewritten emails by practitioner
    """
    body = json.loads(request.data)
    subject = body.get("subject")
    message = body.get("message")
    practitioner_id = body.get("practitioner_id")

    if assert_none([subject, message, practitioner_id]):
        return failure_response("Insufficient inputs", 400)
    
    success, practitioner = dao.get_practitioner_by_id(practitioner_id)

    if not success:
        return failure_response("Practitioner does not exists", 400)
    
    created, email_content = dao.create_email_content(subject, message, practitioner_id)

    if not created:
        return failure_response("Failed to create email", 400)
    

    db.session.add(email_content)
    db.session.commit()
    
    return success_response(email_content.serialize(), 201)
    

@app.route("/emails/prewritten/send/<int:email_id>/", methods = ["POST"])
def send_prewritten_email(email_id):
    """
    Endpoint to send prewritten emails from practitioner to patient

    Precond email_id: is the email id of the email to be sent(integer)
    """
    body = json.loads(request.data)

    practitioner_id = body.get("practitioner_id")
    patient_id = body.get("patient_id")

    if assert_none([practitioner_id, patient_id]):
        return failure_response("Insufficient inputs")
    
    success, patient = dao.get_patient_by_id(patient_id)
    if not success:
        return failure_response("Patient does not exists")
    success, practitioner = dao.get_practitioner_by_id(practitioner_id)
    if not success:
            return failure_response("Practitioner does not exists")
    success, email_content = dao.get_emailcontent_by_id(email_id)
    if not success:
            return failure_response("Email does not exists")
    
    if email_content.practitioner_id != practitioner.id:
        return failure_response("No permission")
    
    sender = os.getenv("GMAIL_SENDER")
    sent, message = email_automater.send_email(email_content.message, email_content.subject, sender, patient.email_address)

    if not sent:
        return failure_response(message)
    
    return success_response({"message" : message,
                             "from" : practitioner_id,
                             "to" : patient_id
                             })


@app.route("/patients/create/", methods = ["POST"])
def create_patient():
    """
    Endpoint to create patient
    """
    body = json.loads(request.data)
    name = body.get("name")
    email_address = body.get("email_address")

    if assert_none([name, email_address]):
        return failure_response("Insufficient inputs", 400)
    
    created, patient = dao.create_patient(name, email_address)

    if not created:
        return failure_response("Failed to create email", 400)
    
    db.session.add(patient)
    db.session.commit()
    
    return success_response(patient.serialize(), 201)


@app.route("/practitioners/create/", methods = ["POST"])
def create_practitioner():
    """
    Endpoint to create practitioner
    """
    body = json.loads(request.data)
    name = body.get("name")
    email_address = body.get("email_address")

    if assert_none([name, email_address]):
        return failure_response("Insufficient inputs", 400)
    
    created, practitioner = dao.create_practitioner(name, email_address)

    if not created:
        return failure_response("Failed to create email", 400)
    
    db.session.add(practitioner)
    db.session.commit()
    
    return success_response(practitioner.serialize(), 201)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
