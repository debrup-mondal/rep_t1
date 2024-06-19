import streamlit as st
from firebase_config import (
    initialize_firebase,
    get_firestore_client,
    get_collection_path,
)
from auth import authenticate, get_all_document_ids
from styles import hide_menu_style

# Apply the CSS to hide the Streamlit menu and footer
st.markdown(hide_menu_style, unsafe_allow_html=True)


# Initialize Firebase
initialize_firebase()


# Get a reference to the Firestore client
db = get_firestore_client()


# Access the collection path from environment variables
collection_path = get_collection_path()


# Fetch the list of all document IDs in the collection
document_list = get_all_document_ids(db, collection_path)


# Main function to run the Streamlit app
def main():
    # Check if user authentication status is in session state, initialize if not
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    # If user is authenticated, show welcome message and title
    if st.session_state.authenticated:
        st.success(f"Welcome {st.session_state.username}")
        st.title("Enter Data Carefully")
    else:
        # If not authenticated, show the login interface
        st.title("Cloud 9 - User Authentication")

        # Create a dropdown select box to choose a username from document list
        username = st.selectbox("Select User", document_list)
        # Create a password input field
        password = st.text_input("Password", type="password")

        # Create a login button
        if st.button("Login"):
            # Authenticate the user when the login button is clicked
            if authenticate(db, collection_path, username, password):
                st.session_state.authenticated = True
                st.session_state.username = username
            else:
                st.warning("Incorrect Password")


# Entry point for the Streamlit app
if __name__ == "__main__":
    main()
