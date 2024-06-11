import streamlit as st

# Title of the app
st.title('Cloud 9')

# Description
st.write('This is an example of a Streamlit app with a selectbox.')

# Define the options for the selectbox
options = ['Option 1', 'Option 2', 'Option 3']

# Create the selectbox
selected_option = st.selectbox('Select an option:', options)

# Display the selected option
st.write(f'You selected: {selected_option}')
