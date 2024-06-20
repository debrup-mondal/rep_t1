import streamlit as st, firebase_admin, json
from firebase_admin import credentials, firestore

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
