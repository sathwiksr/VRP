import string
import random

import datetime

class Citizen:
    def __init__(self,name,age,vaccine_name,dose_num,n_id_type,n_id_num,b_id):
        self.name = name
        self.age = age
        self.vaccine_name = vaccine_name
        self.dose_num = dose_num
        self.n_id_type = n_id_type
        self.n_id_num = n_id_num
        self.b_id = b_id
        self.sb_date = None

def register():
    global rcount
    global b_id_global
    global r_users
    
    print("Enter the following details:")
    name = input("Name: ")
    age = int(input("Age: "))
    vaccine_name = input("Vaccine Name: ")
    dose_num = int(input("Dose Number: "))
    n_id_type = input("National ID Type: ")
    n_id_num = input("National ID Number: ")
    
    b_id = None
    flag=0
    while(True):
        b_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
        if b_id not in b_id_global:
            b_id_global.append(b_id)
            r_user = Citizen(name,age,vaccine_name,dose_num,n_id_type,n_id_num,b_id)
            r_users.append(r_user)
            flag=1
            break
        else:
            print("Working...")
    if(flag):
        print("Successfully Registered! Your Beneficiary ID: ",b_id)

def display():
    global r_users
    flag=0
    b_id = input("Enter Beneficiary ID: ")
    for r_user in r_users:
        if r_user.b_id == b_id:
            flag=1
            print("User found with following details:")
            print("Name:",r_user.name)
            print("Age:",r_user.age)
            print("Vaccine Name:",r_user.vaccine_name)
            print("Dose Number:",r_user.dose_num)
            print("National ID Type:",r_user.n_id_type)
            print("National ID Number:",r_user.n_id_num)
            print("Beneficiary ID:",r_user.b_id)
            print("Slot Booking Date: ",end='')
            if r_user.sb_date:
                print(str(r_user.sb_date)[:10])
            else:
                print("Slot Not Booked Yet")
    if flag==0:
        print("User not registered.")

def bookSlot():
    flag=0
    b_id = input("Enter Beneficiary ID: ")
    for r_user in r_users:
        if r_user.b_id == b_id:
            flag=1
            while True:
                date_string = input('Enter date(dd-mm-yyyy): ')
                try:
                    sb_date = datetime.datetime.strptime(date_string, "%d-%m-%Y")
                except ValueError:
                    print("Invalid date format. Try Again!")
                else:
                    if sb_date>datetime.datetime.now():
                        r_user.sb_date = sb_date
                        print("Slot Booked Successfully!")
                        break
                    else:
                        print("Cannot book slot for this date. Try Again")
            
            
    if flag==0:
        print("User not registered.")

r_users = []
rcount = 0
b_id_global = []

while(True):
    print("Vaccination Monitoring System")
    print("1. Register for vaccine slot")
    print("2. View Info")
    print("3. Total number of registrations")
    print("4. Book Vaccine Slot")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        register()
    elif choice == 2:
        display()
    elif choice == 3:
        print("Total Registered: ",len(r_users))
    elif choice == 4:
        bookSlot()
    else:
        break