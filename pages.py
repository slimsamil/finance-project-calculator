import streamlit as st
import numpy as np
import math

def loan():
    st.header("Loan Calculator")
    years = st.text_input("Years", int())
    amount = st.text_input("Amount of Loan", float())
    interest= st.text_input("Interest as 0.0x", float())
    if st.button("Calculate Loan"):
        try:
            final_amount = float(0)

            for _ in range(0, int(years)):
                if final_amount == 0.0:
                    final_amount = float(amount)

                final_amount = final_amount * (1+float(interest))

            rates = final_amount / (float(years) / 12)

            st.text("\nComplete repayment is {}$".format(round(final_amount,2)))
            st.text("Monthly payment is {}$".format(round(rates,2)))

        except ValueError:
            st.text("Your Input numbers are invalid")


def passbook():
    st.header("Passbook Calculator")

    years = st.text_input("Years")
    amount = st.text_input("Current amount")
    deposit = st.text_input("Monthly deposit")
    interest= st.text_input("Interest as 0.0x")
            
    if st.button("Calculate Passbook"):

        try:
            final_amount = float(0)
            monthly_invest = float(deposit)*12

            for _ in range(0, int(years)):
                if final_amount == 0.0:
                    final_amount = float(amount)

                final_amount = (final_amount+float(monthly_invest))*(1+float(interest))
            st.text("Final amount after {} years: ".format(years) + str(round(final_amount, 2)) + "$")
        except ValueError: 
            st.text("Your Input numbers are invalid")

        st.stop()

def roi():
    st.header("ROI Calculator")
    amount = st.text_input("Loan amount:")
    income = st.text_input("Monthly income:")
    interest = st.text_input("Interest as a decimal number(0.0x):")

    if st.button("Calculate"):
        final_amount = float(amount)
        income = float(income) * 12
        years = int(0)

        for i in range(0, 100):

            final_amount = final_amount * (1+float(interest))
            final_amount = final_amount - income
            if(final_amount <= 0):
                years = i
                break
    
        if(years == 0):
            st.text("\nThe investment is not worth it")
        else:
            st.text("\nThe investment is repaid after {} years".format(years))
        
        st.stop()


