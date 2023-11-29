#jephthah-mensah@email-sender-405509.iam.gserviceaccount.com
from google.oauth2 import service_account
from google_auth_httplib2 import httplib2
from flask import request
from googleapiclient.discovery import build


SCOPES = ['https://www.googleapis.com/auth/sqlservice.admin', 'https://mail.google.com']
SERVICE_ACCOUNT_FILE = './client_secret.json'

creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# print(credentials)
user_info_service = build('oauth2', 'v2', credentials=creds)
user_info = user_info_service.userinfo().get().execute()
print(user_info['email'])


#TODO: looking at how to send and receive email using the api
#TODO: read https://developers.google.com/gmail/api/reference/rest


import base64
from email.message import EmailMessage

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def gmail_create_draft():
  """Create and insert a draft email.
   Print the returned draft's message and id.
   Returns: Draft object, including draft id and message meta data.

  Load pre-authorized user credentials from the environment.
  TODO(developer) - See https://developers.google.com/identity
  for guides on implementing OAuth2 for the application.
  """

  try:
    # create gmail api client
    
    service = build("gmail", "v1", credentials=creds)


    message = EmailMessage()

    message.set_content("This is automated draft mail")

    message["To"] = "jkm255@cornell.edu"
    message["From"] = "jephthah-mensah@email-sender-405509.iam.gserviceaccount.com"
    message["Subject"] = "Automated draft"

    # encoded message
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_message = {"message": {"raw": encoded_message}}
    # pylint: disable=E1101
    draft = (
        service.users()
        .drafts()
        .create(userId="me", body = create_message)
        .execute()
    )

    print(f'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')

  except HttpError as error:
    print(f"An error occurred: {error}")
    draft = None

  return draft


if __name__ == "__main__":
  gmail_create_draft()