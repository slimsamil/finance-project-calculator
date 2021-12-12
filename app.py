import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import loan, passbook, roi

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("Finance Calculator")

# Add all your applications (pages) here
app.add_page("Loan", loan)
app.add_page("Passbook", passbook)
app.add_page("Return of Investment", roi)


# The main app
app.run()