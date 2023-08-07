list = []

def fun1():
    return "Username"
def fun2():
    return "password"
def fun3 ():
    return "Email address"

while True:
    print("Google Login page")
    print("1.login Account")
    print("2.Creat a new Account")
    print("3.Forget password")
    print("4.Back")
    print("Welcome to google official page")
    print("---------------------------------")
    

    option = input("Enter a number between 1-4\n")
    if option == '1':
        print("login Enter your account")
        User_name = input("Enter your username")
        password = input("Enter your  password")
        Email_address = input("Enter an Email")
        list.append(["Username:",User_name, "password:",password,"Email:",Email_address])
        print(list)
        print("Account has been Sucessfully login")
        break
        

    if option == '2':
        print("Creat a account")
        User_name = input("Enter a user name")
        password = input("Enter a password")
        list.append(["Username:",User_name, "password:",password])
        print(list)
        print("New account has been created")
        
        

    if option =='3':
        print("Forget a password")
        User_name = input("Enter your user name")
        Email_address =input("Enter Email Address")
        Otp = int(input("Enter a otp from a Email address"))
        New_password = input("Enter a new password")
        print("Password has been changed")
        

    if option == '4':
        print("Thanks for visiting")
        break

    


    



    
