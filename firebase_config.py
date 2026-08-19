import os
import json
import firebase_admin
from firebase_admin import credentials, firestore


# ==========================================
# FIREBASE INITIALIZATION
# ==========================================

if not firebase_admin._apps:

    # ------------------------------------------
    # OPTION 1: Render Environment Variable
    # ------------------------------------------
    firebase_credentials = os.getenv("FIREBASE_CREDENTIALS")

    if firebase_credentials:
        try:
            firebase_config = json.loads(firebase_credentials)
            cred = credentials.Certificate(firebase_config)

        except json.JSONDecodeError as e:
            raise ValueError(
                f"FIREBASE_CREDENTIALS contains invalid JSON: {e}"
            )

    # ------------------------------------------
    # OPTION 2: Local firebase_key.json
    # ------------------------------------------
    else:
        firebase_file = "firebase_key.json"

        if not os.path.exists(firebase_file):
            raise FileNotFoundError(
                "Firebase credentials not found. "
                "Set FIREBASE_CREDENTIALS in Render Environment Variables "
                "or place firebase_key.json in the project folder."
            )

        cred = credentials.Certificate(firebase_file)

    # Initialize Firebase
    firebase_admin.initialize_app(cred)


# ==========================================
# FIRESTORE DATABASE
# ==========================================

db = firestore.client()