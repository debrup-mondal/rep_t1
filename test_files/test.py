# Replace:
db = firestore.Client.from_service_account_json("firestore-key.json")

# With:
import json

key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="streamlit-reddit")
