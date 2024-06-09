import firebase_admin
from firebase_admin import auth, credentials
import requests
from decouple import config
import json

credentials_url = config("FIREBASE_SERVICE_ACCOUNT")

def initialize_firebase_app():
    response = requests.get(credentials_url)
    firebase_credentials = json.loads(response.content)
    firebase_certificate = credentials.Certificate(firebase_credentials)
    firebase_admin.initialize_app(firebase_certificate)

def firebase_verify_id_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except auth.InvalidIdTokenError:
        return None