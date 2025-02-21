import streamlit as st
import pandas as pd


st.title("User Information Form")

# Initialize session state for storing user data
if "user_data" not in st.session_state:
    st.session_state.user_data = []

# Option buttons for switching between data entry and display
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
        
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            if first_name and last_name and email and phone:
                st.session_state.user_data.append({
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
                })
                st.success("User information added successfully!")
            else:
                st.error("Please fill in required fields: First Name, Last Name, Email, and Phone!")

elif option == "View Data":
    st.header("Stored User Information")
    if st.session_state.user_data:
        df = pd.DataFrame(st.session_state.user_data)
        st.dataframe(df)
    else:
        st.write("No data available.")
