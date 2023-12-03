# #jephthah-mensah@email-sender-405509.iam.gserviceaccount.com
# from google.oauth2 import service_account
# from google_auth_httplib2 import httplib2

# SCOPES = ['https://www.googleapis.com/auth/sqlservice.admin', 'https://mail.google.com']
# SERVICE_ACCOUNT_FILE = './client_secret.json'

# credentials = service_account.Credentials.from_service_account_file(
#         SERVICE_ACCOUNT_FILE, scopes=SCOPES)


#TODO: looking at how to send and receive email using the api
#TODO: read https://developers.google.com/gmail/api/reference/rest

import dao.py
# dao.get_email_by(email_id): gives a str
# dao.get_practitioner_by_id(practitioner_id): gives the practitioner
# dao.get_client_by_id(client_id): gives the client





# Create an object and send the email
class SendEmail:
    def __init__(self, pEmail, cEmail, content):
        self.pEmail = pEmail
        self.cEmail = cEmail
        self.content = content

        
 # send the email: returns (True, message) or (False, message)
import smtplib, ssl
def send_email(pEmail, cEmail, content):
    
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = pEmail  # Enter your address
    receiver_email = cEmail  # Enter receiver address
    password = input("Type your password and press enter: ")
    message = """\{content}."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


 



    
   
    



