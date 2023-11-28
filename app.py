from flask import Flask, request

# Not too sure if this should be here or in db.py
from flask_restful import Resource, Api


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

# Not too sure if this should be here; also open to change based on the db's finilized structure 
class EmailModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    emailAddress = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"EmailModel(name = {name}, emailAddress = {emailAddress})"



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

# Assume that we want all the email responses
def get_all_automatic_email_response():
    """
    Retrieves and returns pre-written email response written by practitioner
    """
    result = EmailModel.query.all()
    return result

# filter response by name
def get_automatic_email_response_by_name(userName):
    """
    Retrieves and returns pre-written email response written by practitioner
    """
    result = EmailModel.query.filter_by(name = userName)
    return result

# filter response by id
def get_automatic_email_response_by_name(userId):
    """
    Retrieves and returns pre-written email response written by practitioner
    """
    result = EmailModel.query.filter_by(id = userId)
    return result

def send_automatic_email_response():
    """
    Sends pre-written email response written by practitioner to client
    """



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
