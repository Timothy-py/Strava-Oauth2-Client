from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload

import requests
import json

from strava_credentials import user_credentials

# ************************** STRAVA API CODES STARTS HERE **************************
# EXCHANGE TOKEN
token_response = requests.post(
    'https://www.strava.com/oauth/token',
    data={
        'client_id': user_credentials['client_id'],
        'client_secret': user_credentials['client_secret'],
        'code': user_credentials['code'],
        'grant_type': 'authorization_code'
    }
)

if token_response.status_code == 200:
    token_response = token_response.json()

    athlete_tokens = {
        'token_type': token_response['token_type'],
        'access_token': token_response['access_token'],
        'refresh_token': token_response['refresh_token'],
        'expires_at': token_response['expires_at'],
        'expires_in': token_response['expires_in'],
        'athlete': token_response['athlete']
    }

    # save the athelete_tokens info in a json file
    with open('stravaUserInfo.json', 'a') as dataObject:
        json.dump(athlete_tokens, dataObject)
    dataObject.close()

    print("Athlete Token Data: {}".format(athlete_tokens))

    # ************************** GOOGLE DRIVE API CODES STARTS HERE **************************
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/drive']

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    drive_service = build('drive', 'v3', credentials=creds)

    # upload file to google drive
    def file_upload(filename, filepath):
        file_metadata = {'name': filename}
        media = MediaFileUpload(filepath)
        file = drive_service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()
        print('File Uploaded Successfully ID: %s' % file.get('id'))


    file_upload('stravaUserInfo.json', 'stravaUserInfo.json')

    # ************************** GOOGLE DRIVE API CODES ENDS HERE **************************

else:
    print("AN ERROR OCCURRED: {}".format(token_response.status_code))

# ************************** STRAVA API CODES ENDS HERE **************************




