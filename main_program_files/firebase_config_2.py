import firebase_admin, os, json, streamlit as st
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def get_collection_path():
    return os.getenv("COLLECTION_PATH")


def initialize_firebase():
    key_dict = json.loads(st.secrets["textkey"])
    creds = service_account.Credentials.from_service_account_info(key_dict)
    db = firestore.Client(credentials=creds, project="fir-projectt1")


def get_firestore_client():
    return firestore.client()
