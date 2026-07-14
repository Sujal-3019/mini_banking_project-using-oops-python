import streamlit as st
import json
from pathlib import Path

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Bank Management System",
    page_icon="🏦",
    layout="wide"
)

DATABASE = "account_db.json"

data = {"Accounts": []}

if Path(DATABASE).exists():
    with open(DATABASE, "r") as f:
        content = f.read()
        if content:
            data = json.loads(content)


def save():
    with open(DATABASE, "w") as f:
        json.dump(data, f, indent=4)


# -----------------------------
# Validation Functions
# -----------------------------

def age_validator(age):
    return age >= 18


def email_validator(email):
    return "@" in email and "." in email


def pin_validator(pin):
    return len(str(pin)) >= 4


# -----------------------------
# Header
# -----------------------------

st.title("🏦 Mini Banking Management System")
st.markdown("---")

menu = st.sidebar.selectbox(
    "Choose Operation",
    (
        "🏠 Home",
        "👤 Register Account",
        "💰 Deposit",
        "💸 Withdraw",
        "📊 Check Balance",
    ),
)

# -----------------------------
# Home
# -----------------------------

if menu == "🏠 Home":

    total_accounts = len(data["Accounts"])

    total_balance = sum(acc["balance"] for acc in data["Accounts"])

    c1, c2 = st.columns(2)

    c1.metric("Total Accounts", total_accounts)

    c2.metric("Total Bank Balance", f"₹ {total_balance}")

    st.markdown("---")

    st.info("Select an operation from the sidebar.")


# -----------------------------
# Register
# -----------------------------

elif menu == "👤 Register Account":

    st.header("Create New Account")

    with st.form("register"):

        name = st.text_input("Full Name")

        age = st.number_input("Age", min_value=18, step=1)

        email = st.text_input("Email")

        pin = st.text_input("4 Digit PIN", type="password")

        account_number = st.number_input(
            "Account Number",
            min_value=1,
            step=1,
            format="%d",
        )

        submit = st.form_submit_button("Create Account")

    if submit:

        for account in data["Accounts"]:
            if account["account_number"] == account_number:
                st.error("Account Number already exists.")
                st.stop()

        if not age_validator(age):
            st.error("Age must be at least 18.")
            st.stop()

        if not email_validator(email):
            st.error("Invalid Email.")
            st.stop()

        if not pin_validator(pin):
            st.error("PIN should be at least 4 digits.")
            st.stop()

        data["Accounts"].append(
            {
                "name": name,
                "age": age,
                "email": email,
                "pin": int(pin),
                "account_number": account_number,
                "balance": 0,
            }
        )

        save()

        st.success("✅ Account Created Successfully!")


# -----------------------------
# Deposit
# -----------------------------

elif menu == "💰 Deposit":

    st.header("Deposit Money")

    account = st.number_input(
        "Account Number",
        min_value=1,
        step=1,
        format="%d",
    )

    pin = st.text_input("PIN", type="password")

    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):

        found = False

        for acc in data["Accounts"]:

            if acc["account_number"] == account:

                found = True

                if acc["pin"] != int(pin):
                    st.error("Incorrect PIN")
                    break

                acc["balance"] += amount

                save()

                st.success(f"₹{amount} Deposited Successfully")

                st.info(f"Current Balance : ₹{acc['balance']}")

                break

        if not found:
            st.error("Account Not Found")


# -----------------------------
# Withdraw
# -----------------------------

elif menu == "💸 Withdraw":

    st.header("Withdraw Money")

    account = st.number_input(
        "Account Number",
        min_value=1,
        step=1,
        format="%d",
    )

    pin = st.text_input("PIN", type="password")

    amount = st.number_input("Withdrawal Amount", min_value=1)

    if st.button("Withdraw"):

        found = False

        for acc in data["Accounts"]:

            if acc["account_number"] == account:

                found = True

                if acc["pin"] != int(pin):
                    st.error("Incorrect PIN")
                    break

                if amount > acc["balance"]:
                    st.error("Insufficient Balance")
                    break

                acc["balance"] -= amount

                save()

                st.success(f"₹{amount} Withdrawn Successfully")

                st.info(f"Remaining Balance : ₹{acc['balance']}")

                break

        if not found:
            st.error("Account Not Found")


# -----------------------------
# Balance
# -----------------------------

elif menu == "📊 Check Balance":

    st.header("Account Balance")

    account = st.number_input(
        "Account Number",
        min_value=1,
        step=1,
        format="%d",
    )

    pin = st.text_input("PIN", type="password")

    if st.button("Show Balance"):

        found = False

        for acc in data["Accounts"]:

            if acc["account_number"] == account:

                found = True

                if acc["pin"] != int(pin):
                    st.error("Incorrect PIN")
                    break

                st.success("PIN Verified")

                st.metric("Current Balance", f"₹ {acc['balance']}")

                break

        if not found:
            st.error("Account Not Found")