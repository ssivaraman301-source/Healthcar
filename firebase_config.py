import firebase_admin
from firebase_admin import credentials, firestore


# ==========================================
# FIREBASE INITIALIZATION
# ==========================================

if not firebase_admin._apps:

    cred = credentials.Certificate(
        "firebase_key.json"
    )

    firebase_admin.initialize_app(cred)


# ==========================================
# FIRESTORE DATABASE
# ==========================================

db = firestore.client()