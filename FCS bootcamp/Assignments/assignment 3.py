number = int(input("Enter number of students: "))

students = []

for i in range(number):
    student = input("Enter student " + str(i+1) + " name: ")
        
    while True:
        grade = int(input("Enter " + str(student) + "'s score: "))
        if 0 <= grade <= 100:
            break
        else:
            print("Invalid input")
                       
    student_info = (student, grade)
    students.append((student_info))
                
print("students =", students)