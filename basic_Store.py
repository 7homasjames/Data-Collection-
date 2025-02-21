import streamlit as st
import pandas as pd
import json
import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

# Load environment variables
load_dotenv()
BLOB_CONNECTION_STRING = os.getenv("BLOB_CONNECTION_STRING")  # Load from .env
CONTAINER_NAME = os.getenv("CONTAINER_NAME")  # Load from .env

# Function to upload data to Azure Blob Storage
def upload_to_blob_storage(data, blob_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(BLOB_CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)
        
        json_data = json.dumps(data)
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(json_data, overwrite=True)
        
        st.success(f"Data successfully uploaded to blob: {blob_name}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

st.title("User Information Form")

# Initialize session state for storing user data
if "user_data" not in st.session_state:
    st.session_state.user_data = []

with st.sidebar:
    option = st.radio("Choose an option:", ["Enter Data", "View Data"])

if option == "Enter Data":
    st.header("Enter User Information")
    with st.form("user_form"):
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        career = st.text_input("Career")
        years_experience = st.selectbox("Years of Experience", ["0-1", "2-5", "6-10", "10+"])
        license = st.text_input("License")
        education = st.text_input("Education/Degree")
        linkedin = st.text_input("LinkedIn Link")
        country = st.selectbox("Country", ["USA", "Canada", "UK", "Other"])
        state = st.selectbox("State", ["State 1", "State 2", "State 3", "Other"])
        city = st.text_input("City")
        zip_code = st.text_input("Zip Code")
        current_status = st.text_input("Current Status")
        need_sponsor = st.radio("Need Sponsor?", ["Yes", "No"])
        contract_other_company = st.selectbox("Contract with other company?", ["Yes", "No"])
        ready_to_relocate = st.selectbox("Ready to Relocate", ["Yes", "No"])
        university = st.text_input("University")
        graduation_year = st.text_input("Graduation Year")
        expected_rate = st.text_input("Expected Per Hour Rate")
        employment_type = st.multiselect("Employment Type", ["Full-time", "Part-time", "Contract", "Internship"])
        reference1 = st.text_input("Reference 1")
        reference2 = st.text_input("Reference 2")
        
        storage_option = st.radio("Select storage option:", ["Local Storage", "Azure Blob Storage"])
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            if first_name and last_name and email and phone:
                user_data = {
                    "First Name": first_name,
                    "Last Name": last_name,
                    "Email": email,
                    "Phone": phone,
                    "Career": career,
                    "Years of Experience": years_experience,
                    "License": license,
                    "Education/Degree": education,
                    "LinkedIn Link": linkedin,
                    "Country": country,
                    "State": state,
                    "City": city,
                    "Zip Code": zip_code,
                    "Current Status": current_status,
                    "Need Sponsor": need_sponsor,
                    "Contract with other company": contract_other_company,
                    "Ready to Relocate": ready_to_relocate,
                    "University": university,
                    "Graduation Year": graduation_year,
                    "Expected Per Hour Rate": expected_rate,
                    "Employment Type": ", ".join(employment_type),
                    "Reference 1": reference1,
                    "Reference 2": reference2
                }
                
                if storage_option == "Local Storage":
                    st.session_state.user_data.append(user_data)
                    st.success("User information added locally!")
                else:
                    blob_name = f"user_data_{email.replace('@', '').replace('.', '')}.json"
                    upload_to_blob_storage(user_data, blob_name)
                    st.session_state.user_data.append(user_data)
            else:
                st.error("Please fill in required fields: First Name, Last Name, Email, and Phone!")

elif option == "View Data":
    st.header("Stored User Information")
    if st.session_state.user_data:
        df = pd.DataFrame(st.session_state.user_data)
        st.dataframe(df)
    else:
        st.write("No data available.")
