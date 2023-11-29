from flask import Flask, request
from db import db
import email_automater
import json
db_filename = "culturecare.db"
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.drop_all()
    db.create_all()

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
    Sends pre-written email response written by practitioner to client
    """
# end point to create emails
#email_automater.send_email(client_id, practitiner_id, email_id)
@app.route("/email/send/prewritten/<int:email_id/", methods = ["POST"])
def send_prewritten_email(email_id):
    """
    Endpoint to send prewritten emails from practitioner to client

    Precond email_id: is the email id of the email to be sent(integer)
    """
    body = json.loads(request.data)
    
    data = body.get("client_id") #gets the value 
    total_rejected_ballots = body.get("total_rejected_ballots")
    total_votes_cast = body.get("total_votes_casts")
    total_valid_ballots = body.get("total_valid_ballots")
    pink_sheet = body.get("pinksheet")
    auto_password = body.get("auto_password")
    polling_station_id = body.get("polling_station_id")
    data, success_code = secret_message()

    if success_code != 201 or json.loads(data) != "Session verified!":
        return failure_response("Session expired", 400)

    provided_all_data = data and total_rejected_ballots and total_votes_cast and total_valid_ballots and pink_sheet and auto_password and polling_station_id
    if not (provided_all_data):
        return failure_response("Invalid inputs!", 400)
    
    created, polling_station_result = dao.create_polling_station_result(data, 
                                                                        total_votes_cast, 
                                                                        total_rejected_ballots,
                                                                        total_valid_ballots,
                                                                        pink_sheet,
                                                                        polling_agent_id,
                                                                        polling_station_id,
                                                                        auto_password)
    
    if not created:
        return failure_response("Couldn't create result", 400)
    
    return success_response(polling_station_result.serialize(), 201)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
