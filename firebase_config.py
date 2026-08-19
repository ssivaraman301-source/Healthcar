import os
import json
import firebase_admin
from firebase_admin import credentials, firestore


if not firebase_admin._apps:

    firebase_credentials = os.getenv("FIREBASE_CREDENTIALS")

    if firebase_credentials:
        firebase_config = json.loads(firebase_credentials)
        cred = credentials.Certificate(firebase_config)
    else:
        cred = credentials.Certificate("firebase_key.json")

    firebase_admin.initialize_app(cred)


db = firestore.client()