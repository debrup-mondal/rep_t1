import firebase_admin
from firebase_admin import credentials, firestore
import json
import streamlit as st

COLLECTION_PATH = "testCollection"


def get_collection_path():
    return COLLECTION_PATH


def initialize_firebase():
    if not firebase_admin._apps:
        key_dict = json.loads(st.secrets["textkey"])
        creds = credentials.Certificate(key_dict)
        firebase_admin.initialize_app(creds)


def get_firestore_client():
    return firestore.client()


# Usage Example
if __name__ == "__main__":
    initialize_firebase()
    db = get_firestore_client()
    collection_path = get_collection_path()
    # Now you can use 'db' to interact with Firestore, e.g., db.collection(collection_path).get()
