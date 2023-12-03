from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import dotenv
dotenv.load_dotenv()


def send_email(email_body, subject, sender, receiver):
    """
    Sends email(content) from sender to receiver

    Precond receiver: is the email address of the receiver
    Precond sender: is the email address of the sender
    Precond subject: is the subject of the email(str)
    Precond email: is the body of the email(str)
    """
    CLIENT_SECRET_FILE = os.getenv("GMAIL_CLIENT_SECRET_FILE")
    GMAIL_SCOPES = os.getenv("GMAIL_SCOPES")
    service = Create_Service(CLIENT_SECRET_FILE, 'gmail', 'v1', GMAIL_SCOPES)

    emailMsg = email_body
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = receiver
    mimeMessage['subject'] = subject
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
    
    try:
        message = service.users().messages().send(userId= sender, body={'raw': raw_string}).execute()
    except:
        return False, "Failed to send message"
    return True, "Sent message successfully"

