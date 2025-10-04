number = int(input("Enter a number:"))
is_prime = True
if number < 2:
    print(number, "is not a prime number")
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    
if is_prime:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")