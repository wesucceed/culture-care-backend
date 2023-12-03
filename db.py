"""
The database of culture care api
"""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class EmailContent(db.Model):
    """
    EmailContent Model
    """
    __tablename__ = "emailcontents"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    message = db.Column(db.String)
    practitioner_id = db.Column(db.Integer, db.ForeignKey("practitioners.id"), nullable = False)
    subject = db.Column(db.String)



    def __init__(self, **kwargs):
        """
        Initializes a EmailContent object
        """
        self.message = kwargs.get("message")
        self.subject = kwargs.get("subject")
        self.practitioner_id = kwargs.get("practitioner_id")

    def simple_serialize(self):
        """
        Simple serializes an emailcontent object
        """
        return {
            "id" : self.id,
            "message" : self.message,
            "subject" : self.subject,
            "practitioner_id" : self.practitioner_id
        }
    
    def serialize(self):
        """
        Serializes an emailcontent object
        """
        return {
            "id" : self.id,
            "message" : self.message,
            "subject" : self.subject,
            "practitioner_id" : self.practitioner_id
        }


class Patient(db.Model):
    """
    Patient Model
    """
    __tablename__ = "patients"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    name = db.Column(db.String, nullable = False)
    email_address = db.Column(db.String, nullable = False, unique = True)


    def __init__(self, **kwargs):
        """
        Initializes a Patient object
        """
        self.name = kwargs.get("name")
        self.email_address = kwargs.get("email_address")

    def simple_serialize(self):
        """
        Simple serializes a patient object
        """
        return {
            "id" : self.id,
            "name" : self.name,
            "email_address" : self.email_address,
        }


class Practitioner(db.Model):
    """
    Practitioner Model
    """
    __tablename__ = "practitioners"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    name = db.Column(db.String, nullable = False)
    email_address = db.Column(db.String, nullable = False, unique = True)
    emailcontents = db.relationship("EmailContent")  

    def __init__(self, **kwargs):
        """
        Initializes a Practitioner object
        """
        self.name = kwargs.get("name")
        self.email_address = kwargs.get("email_address")

    def simple_serialize(self):
        """
        Simple serializes a practitioner object
        """
        return {
            "id" : self.id,
            "name" : self.name,
            "email_address" : self.email_address,
        }


