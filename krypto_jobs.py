################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
from inspect import getfullargspec

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
################################################################################
# Step 1:
# Import Ethereum Transaction Functions into the KryptoJobs2Go Application

# Import several functions from the `crypto_wallet.py` script into the file 
# `krypto_jobs.py`, which contains code for Fintech Finder's customer 
# interface, in order to add wallet operations to the application. For this 
# section, you will assume the perspective of a Fintech Finder customer 
# (i.e., you'll provide your Ethereum wallet and account information to the 
# application).

# Complete the following steps:

# 1. Import the following functions from the `crypto_wallet.py` file:
# * `generate_account`
# * `get_balance`
# * `send_transaction`

# 2. Within the Streamlit sidebar section of code, create a variable named
# `account`. Set this variable equal to a call on the `generate_account`
# function. This function will create the KryptoJobs2Go customer's (in this
# case, your) HD wallet and Ethereum account.

# 3. Within this same section of the `krypto_jobs.py` file, define a
# new `st.sidebar.write` function that will display the balance of the
# customer's account. Inside this function, call the `get_balance` function
# and pass it your Ethereum `account.address`.

################################################################################
# Step 1 - Part 1
# Import the following functions from the `crypto_wallet.py` file:
# * `generate_account`
# * `get_balance`
# * `send_transaction`

from crypto_wallet import generate_account, get_balance, send_transaction

################################################################################
# KryptoJobs2Go Candidate Information

# Database of KryptoJobs2Go candidates including their name, digital address, rating and hourly cost per Ether.
# A single Ether is currently valued at $1,500
candidate_database = {
    "Lane": [
        "Lane",
        "0x4a5f289CF41451Cbe31949641AB828223F5029A4",
        "4.3",
        0.20,
        "Images/lane.jpeg",
    ],
    "Ash": [
        "Ash",
        "0xadc1ab52e2d401F38A70ef25451ff713fc4550A5",
        "5.0",
        0.33,
        "Images/ash.jpeg",
    ],
    "Jo": [
        "Jo",
        "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45",
        "4.7",
        0.19,
        "Images/jo.jpeg",
    ],
    "Kendall": [
        "Kendall",
        "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45",
        "4.1",
        0.16,
        "Images/kendall.jpeg",
    ],
}

# A list of the KryptoJobs2Go candidates first names
people = ["Lane", "Ash", "Jo", "Kendall"]


def get_people(w3):
    """Display the database of KryptoJobs2Go candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("KryptoJobs2Go Rating: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")


################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# KryptoJobs2Go!")
st.markdown("## Hire A Fintech Professional!")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

##########################################
# Step 1 - Part 2:
# Create a variable named `account`. Set this variable equal to a call on the
# `generate_account` function. This function will create the KryptoJobs2Go
# customer's (in this case, your) HD wallet and Ethereum account.

account = generate_account()

##########################################

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

##########################################
# Step 1 - Part 3:
# Define a new `st.sidebar.write` function that will display the balance of the
# customer's account. Inside this function, call the `get_balance` function and
#  pass it your Ethereum `account.address`.

st.sidebar.write(get_balance(w3, account.address))

##########################################

# Create a select box to chose a FinTech Hire candidate
person = st.sidebar.selectbox("Select a Person", people)

# Create a input field to record the number of hours the candidate worked
hours = st.sidebar.number_input("Number of Hours")

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

# Identify the FinTech Hire candidate
candidate = candidate_database[person][0]

# Write the KryptoJobs2Go candidate's name to the sidebar
st.sidebar.write(candidate)

# Identify the KryptoJobs2Go candidate's hourly rate
hourly_rate = candidate_database[person][3]

# Write the inTech Finder candidate's hourly rate to the sidebar
st.sidebar.write(hourly_rate)

# Identify the KryptoJobs2Go candidate's Ethereum Address
candidate_address = candidate_database[person][1]

# Write the inTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write(candidate_address)

# Write the KryptoJobs2Go candidate's name to the sidebar

st.sidebar.markdown("## Total Wage in Ether")

################################################################################
# Step 2: Sign and Execute a Payment Transaction

# Complete the following steps:
#########################################

# Step 2 - Part 1:
# * Write the equation that calculates the candidate's wage. This equation
# should assess the candidate's hourly rate from the candidate database
# (`candidate_database[person][3]`) and then multiply this hourly rate by
# the value of the `hours` variable. Save this calculation's output as a
# variable named `wage`.

wage = candidate_database[person][3] * hours

# Streamlit Code

st.sidebar.write(wage)

##########################################
# Step 2 - Part 2:
# * Call the `send_transaction()` function and pass it three parameters:
# - Your Ethereum `account` information. (Remember that this `account`
# instance was created when the `generate_account` function was called.)
#  From the `account` instance, the application will be able to access the
#  `account.address` information that is needed to populate the `from` data
# attribute in the raw transaction.
# - The `candidate_address` (which will be created and identified in the
# sidebar when a customer selects a candidate). This will populate the `to`
# data attribute in the raw transaction.
# - The `wage` value. This will be passed to the `toWei` function to
# determine the wei value of the payment in the raw transaction.

if st.sidebar.button("Send Transaction"):

    transaction_hash = send_transaction(w3, account, candidate_address, wage)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes KryptoJobs2Go candidates to the Streamlit page
get_people(w3)