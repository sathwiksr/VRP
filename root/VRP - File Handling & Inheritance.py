class LoginUser:
    def __init__(self,username,password):
        self.username = username
        self.password = password

class Citizen(LoginUser):
    def __init__(self,username,password,name,age,vaccine_name,dose_num,n_id_type,n_id_num,b_id):
        self.name = name
        self.age = age
        self.vaccine_name = vaccine_name
        self.dose_num = dose_num
        self.n_id_type = n_id_type
        self.n_id_num = n_id_num
        self.b_id = b_id
        self.sb_date = None
        LoginUser.__init__(self,username,password)

def display():
    pstr = "\nUsername: " + r_user.username + "\nPassword: " + r_user.password + "\nName: " + r_user.name + "\nAge: " + r_user.age + "\nVaccine Name: " + r_user.vaccine_name + "\nDose Number: " + r_user.dose_num + "\nNational ID Type: " + r_user.n_id_type + "\nNational ID Number: " + r_user.n_id_num + "\nSlot Booking Date: "

    if r_user.sb_date:
        pstr += str(r_user.sb_date)[:10]
    else:
        pstr += "Slot Not Booked Yet"
        
    return pstr
    
while(True):
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username == "gs" and password == "pass":
        r_user = Citizen(username,password,"Gaurav", "23",  "Covishield", "1", "Aadhar Card", "123456789", "AB12345")
        while(True):
            try:
                file = open('citizen.txt','r+')
                file.seek(0)
                file.write("Citizen Record: \n" + display() )
                file.seek(0)
                data = file.read()
                print(data)
            except:
                file = open('citizen.txt','w')
                file.close()
            else:
                file.close()
                break
        break
    else:
        print("Wrong Credentials! Try Again")