import json
from pathlib import Path


database = "account_db.json"
data = {"Accounts":[]}

if Path(database).exists():
    with open(database) as f:
        content = f.read()
        if content:
            data = json.loads(content)

def save():
    with open(database , "w") as f:
        json.dump(data,f,indent=4)

def age_validater(age):
    if age>=18:
        return True
    else:
        return False
    
def email_validater(email):
    if "@" in email and "." in email :
        return True
    else :
        return False

def pin_validater(pin):
    if len(str(pin))>4:
        return True
    else:
        return False


class Register:
    def register_account(self):
        try:
            name = input("Enter the Name : ")
        except ValueError:
            print("Invalid Name format! try again\n")
            return
        try:
            age = int(input("Enter the age: "))
        except ValueError:
            print("Invalid age Format ! try again \n")
            return
        try:
            email = input("Enter your email : ")
        except:
            print("Invalid Mail Format! try again\n")
            return
        try:
            pin = int(input("Create your Pin(more than 4 digit) : "))
        except ValueError:
            print("Invalid pin ! try again\n")
            return
        try:
            account_number= int(input("Enter the account number : "))
        except ValueError:
            print("Invalid Account number format! try again\n")
            return
        for i in data["Accounts"]:
            if i['account_number']==account_number:
                print("Account Number already exists ! Try again")
                return
        if age_validater(age) and email_validater(email) and pin_validater(pin):
            print("Account Created Successfully \n")
        else:
            print("There is some error from your side while regestring , Please Retry :(")
            return False 
        
        data["Accounts"].append({
            "name" : name,
            "age" : age,
            "email" : email,
            "pin" : pin,
            "account_number" : account_number ,
            "balance": 0
        })
        save()

class w:
    def withdraw(self):
        account_number = int(input("Enter your Account Number : "))
        for i in data['Accounts']:
            if i['account_number'] == account_number:
                pin = int(input("Enter the pin : ")) 
                if i['pin'] == pin :
                    print("pin verified successfully")
                    try:
                        withdraw_ammount = int(input("Enter amount to be withdrawn : "))
                    except ValueError:
                        print("Invalid Format !try again")
                        return
                    if withdraw_ammount <= i['balance']:
                        if withdraw_ammount >=1:
                            i["balance"]-= withdraw_ammount 
                            save()
                        else:
                            print("Withdrawl ammount must be greater than 0")
                            return
                        print(f"Withdrawing {withdraw_ammount} rupees")
                        print(f"Remaing Balance in Account : {i['balance']} \n")
                    else :
                        print("Not enough Balance")
                else:
                    print("Incorrect Pin for accessing the Account ! Try Again ")
                return
        print("Incorrect Account Number! Try Again")

class depo :
    def deposit(self):
        account_number = int(input("Enter your Account Number : "))
        for i in data["Accounts"]:
            if i['account_number'] == account_number:
                pin = int(input("Enter the pin :"))
                if i['pin']==pin:
                    print("Pin verified Successfully")
                    try:
                        deposit_ammount = int(input("Enter the amount to be deposited : "))
                    except ValueError:
                        print("Invalid Format! try again")
                        return
                    if deposit_ammount >=1:
                        i['balance']+=deposit_ammount
                        save()
                    else:
                        print("Deposited amount must be greater than 0")
                        return
                    print(f"{deposit_ammount} rupees deposited successfully")
                    print(f"Now your total balance is {i['balance']} \n")
                else:
                    print("Incorrect Pin for accessing the Account ! Try Again")
                return
        print("Incoorect Account Number : Try Again")

class show:
    def show_info(self):
        account_number=int(input("Enter the Account Number: "))
        for i in data["Accounts"]:
            if i["account_number"] == account_number:
                pin = int(input("Enter the pin :"))
                if i['pin']==pin:
                    print("Pin verified Successfully")
                    print(f"your total balance is {i['balance']} \n")
                else:
                    print("Incoorect Pin for the Account! Try Again ")
                return
        print("Incorrect Account Number! Try again")

user = Register()
wi = w()
de = depo()
sh = show()
while True: 
    print("Enter 1 for Registering an Account")
    print("Enter 2 for depositing in an Account")
    print("Enter 3 for withdrawing from Account")
    print("Enter 4 for viewing balance of an Account")
    print("Enter 5 to exit")
    try:
        choice = int(input("Enter your Choice : "))
    except Exception as e:
        print("Invalid Choice format! try again")
        continue
    if choice == 1:
        user.register_account()

    elif choice == 2:
        de.deposit()

    elif choice == 3:
        wi.withdraw()

    elif choice == 4 :
        sh.show_info()

    elif choice == 5 :
        break
    else:
        print("Choice is not valid")