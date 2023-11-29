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

# send the email: returns (True, message) or (False, message)
