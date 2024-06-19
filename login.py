''' write a pg to build login system usig functions.the function name should be login and register
 1.it should ask user to enter the details for registration and out of all these detials only 
user name and passwrd should be stored.  
 2.now this functoion should ask user  usernsme name and passwd if these match 
with the rgistred details login success otherwise repeat the login processsaying that its invalid'''

def login():
    d=[]
    print("welcome to reg")
    uname=input("enter user name")
    upass=input("enter the passwd")
    name=input("enter name")
    phno=input("enter phno")
    
    d[uname]=upass
    while True:
        print("welcm to login")
        iname=input("enter user login")
        ipass=input("enter login passwd")
        if iname in d:
            if d[iname]==ipass:
                print("login success")
                break
            else:
                print("enter valid passcode")
        else:
            print("user not found")
            break
     
    