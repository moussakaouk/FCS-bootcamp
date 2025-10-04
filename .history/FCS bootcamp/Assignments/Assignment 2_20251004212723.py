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
        N = int(input("Enter a number: "))
        print("Prime numbers between 2 and", N, "are:")

        for num in range(2, N + 1):        # loop through all numbers from 2 to N
            is_prime = True                # assume each number is prime
            for i in range(2, num):        # test all numbers from 2 to num-1
                if num % i == 0:           # if divisible
                    is_prime = False       # not prime
                    break
            if is_prime:
                print(num) 

        loggedin = True
        break
    else:
        attempts += 1
if attempts < max_attempts:
    print(max_attempts - attempts, "attempt(s) left")
        
if not loggedin:
    print("Account Locked")
        