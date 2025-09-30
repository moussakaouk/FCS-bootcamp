for i in range(5):
    print(i, end=" ")


for i in range(0,10,1):
    print(i, end=" ")

start = 0
stop = 10
step = 2

print()

for i in range(start, stop, step):
    print(i, end =" ")


for rows in range(1,6):
    if rows == 3:
        break
    for columns in range(1,6):
        print(rows*columns, end=" ")
    print()
        


total = 0 

while True:
    number = int(input("Enter a number (-1 to quit): "))
    print("The total now is: ",total)
    if number == -1:
        break
    total = total + number 
    print("The total at the end is now: ",total)

print("total: ",total)



number = 7

while True:
    if number == 7:
        print("You guessed it right!")
        break
