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
        

