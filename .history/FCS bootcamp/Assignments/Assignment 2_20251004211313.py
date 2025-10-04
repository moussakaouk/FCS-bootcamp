stored_username = "admin"
stored_password = "1234"
attempts = 0
max_attempts = 3
loggedin = False

while attempts < max_attempts:
    username = input("Enter your username:")
    password = input("Enter your password:")
    if username == stored_username and password == stored_password:
        print("Welcome back")
        loggedin = True
        break
    else:
        nbofatmpts = 2 - attempts
        attempts = attempts + 1
        print(nbofatmpts,"attempt left")

        
if not loggedin:
    print("Account Locked")
        