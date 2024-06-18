import firebase_admin, os
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Path to your service account key JSON file
cred_path = os.getenv("CRED_PATH")


def get_collection_path():
    return os.getenv("COLLECTION_PATH")


def initialize_firebase():
    if cred_path is None:
        raise ValueError("CRED_PATH environment variable not set")

    # Check if the Firebase app is already initialized to avoid reinitialization
    if not firebase_admin._apps:
        # Initialize Firebase app with service account credentials
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)


def get_firestore_client():
    return firestore.client()
