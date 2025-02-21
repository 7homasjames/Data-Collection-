# Streamlit User Information Form

## Overview
This is a Streamlit application that allows users to enter and store basic personal information. The data is displayed in a table format for easy reference.

## Features
- **Sidebar Navigation:** Users can select between "Enter Data" and "View Data."
- **Data Entry Form:** Users can enter various personal details such as name, email, career, location, and employment details.
- **Data Storage:** Information is stored in Streamlit's session state.
- **Table View:** Stored user data is displayed in a structured table format.

## Installation
1. Ensure you have Python installed.
2. Install Streamlit and Pandas if not already installed:
   ```sh
   pip install streamlit pandas
   ```

## Running the Application
To start the Streamlit app, run the following command:
```sh
streamlit run app.py
```
Replace `app.py` with the filename of your script if different.

## Usage
1. Open the app in a web browser after running the command.
2. Select "Enter Data" in the sidebar to input personal details.
3. Click "Submit" to save the entered data.
4. Switch to "View Data" in the sidebar to see all stored entries.

## Requirements
- Python 3.7+
- Streamlit
- Pandas

## Customization
To modify dropdown options or add more fields, edit the form fields in the `app.py` script accordingly.

## License
This project is open-source and available for modification as needed.


