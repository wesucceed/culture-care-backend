"""
A module to access data from database
"""
from db import Patient, Practitioner, EmailContent

def get_patient_by_id(patient_id):
    """
    Returns patient with patient_id
    """

    return Patient.query.filter(Patient.id == patient_id).first()

def get_practitioner_by_id(practitioner_id):
    """
    Returns practitioner with practitioner_id
    """
    return Practitioner.query.filter(Practitioner.id == practitioner_id)

def get_emailcontent_by_id(emailcontent_id):
    """
    Returns emailcontent with emailcontent_id
    """
    return EmailContent.query.filter(EmailContent.id == emailcontent_id)

