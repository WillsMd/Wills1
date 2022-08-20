import hashlib
def Signup():
    email=input("Enter your email address:")
    pwd=input("Enter your password: ")
    conf_pwd=input("Confirm your password:")
    
    if conf_pwd==pwd:
        enc=conf_pwd.encode()
        hash1=hashlib.md5(enc).hexdigest()
        
        with open("credentials.txt", "w") as f:
            f.write(email + "\n")
            f.write(hash1)
        f.close()
        print("You have registered successfully")
        
    else:
        print("Password is not the same as above! \n")
        
def login():
    email=input("Enter your email:")
    pwd=input("Enter your password:")
    
    auth=pwd.encode()
    auth_hash=hashlib.md5(auth).hexdigest()
    with open("credentials.txt", "r") as f:
        stored_email, stored_pwd =f.read().split("\n")
    f.close()
    
    if email==stored_email and auth_hash == stored_pwd:
        print("login in Successfully!")
    else:
        print("Login failed!\n")
        
while 1:
    print("***************login System**********")
    print("1.Sign Up")
    print("2.Login")
    print("3.Exit")
    ch=int(input("Enter your choice:"))
    if ch ==1:
        Signup()
    elif ch==2:
        login()
    elif ch==3:
        break
    else:
        print("Invalid")
        exit()        
                         
                
            
