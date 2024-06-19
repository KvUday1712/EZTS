''' write a pg to build login system usig functions.the function name should be login and register
 1.it should ask user to enter the details for registration and out of all these detials only 
user name and passwrd should be stored.  
 2.now this functoion should ask user  usernsme name and passwd if these match 
with the rgistred details login success otherwise repeat the login processsaying that its invalid'''

def login():
    users = {}  
    print("Welcome to registration")
    
    uname = input("Enter username: ")
    upass = input("Enter password: ")
    name = input("Enter name: ")
    phno = int(input("Enter phone number: "))
    
    users[uname] = upass
    
    while True:
        print("Welcome to login")
        iname = input("Enter username: ")
        ipass = input("Enter password: ")
        
        if iname in users:
            if users[iname] == ipass:
                print("Login successful")
                break
            else:
                print("Invalid password, please try again")
        else:
            print("User not found, please try again")
            break
login()

     
    
