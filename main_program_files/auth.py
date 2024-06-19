import hashlib
import streamlit as st


# Function to fetch all document IDs in the specified Firestore collection
def get_all_document_ids(db, collection_path):
    docs = db.collection(collection_path).stream()
    return [doc.id for doc in docs]


# Function to hash a password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Function to authenticate a user by username and password
def authenticate(db, collection_path, username, password):
    try:
        # Attempt to fetch user document from Firestore
        user_ref = db.collection(collection_path).document(username)
        user_doc = user_ref.get()

        if user_doc.exists:
            # Extract user data from the document
            user_data = user_doc.to_dict()
            stored_password = user_data.get("Password")
            # Hash the input password
            hashed_password = hash_password(password)
            # Check if the hashed input password matches the stored hashed password
            if hashed_password == stored_password:
                return True
            else:
                return False
        else:
            st.error("User document does not exist")
            return False
    except Exception as e:
        st.error(f"Error: {e}")
        return False
