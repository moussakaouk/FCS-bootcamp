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
        number = int(input("Enter a number"))
        print("Prime number between 2 and", n)

        loggedin = True
        break
    else:
        attempts += 1
if attempts < max_attempts:
    print(max_attempts - attempts, "attempt(s) left")
        
if not loggedin:
    print("Account Locked")
        