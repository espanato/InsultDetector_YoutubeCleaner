import click
import random
import csv
import os
import pickle
import time
import sys
from google.auth import credentials
import google.oauth2.credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from pathlib import Path


#SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
#SCOPES = ['http://sharepoint/content/sitecollection/web']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
HOME = str(Path.home())
CACHE_CREDENTIALS_DIR = '.'
CACHE_CREDENTIALS_FILE = CACHE_CREDENTIALS_DIR + 'token.pickle'


def get_authenticated_service(CLIENT_SECRETS_FILE):
    credentials = None

    # check if creds path exist
    if not os.path.exists(CACHE_CREDENTIALS_DIR):
        os.makedirs(CACHE_CREDENTIALS_DIR)

    # check if creds file exists
    if os.path.exists(CACHE_CREDENTIALS_FILE):
        with open(CACHE_CREDENTIALS_FILE, 'rb') as token:
            credentials = pickle.load(token)

    # check if the credentials are invalid or do not exist
    if not credentials or not credentials.valid:

        # check if the credentials have expiredq
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())

        else:
            # else auth by google
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE, SCOPES)
            credentials = flow.run_console()

        # Save the credentials into the pickle for the next run
        with open(CACHE_CREDENTIALS_FILE, 'wb') as token:
            pickle.dump(credentials, token)

    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


service = get_authenticated_service('credentials.json')
