import streamlit as st


# Main function to run the Streamlit app
def main():

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if st.session_state.authenticated:
        st.title("Article 2")
    else:
        st.title("Article 1")
        username = st.text_input("username")

        if username == "a":
            st.session_state.authenticated = True
            st.rerun()  # Rerun the app to display Article 2 without Article 1 and the text box


# Entry point for the Streamlit app
if __name__ == "__main__":
    main()
