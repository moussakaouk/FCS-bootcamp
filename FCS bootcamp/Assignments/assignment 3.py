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

print("All students and scores: ")

for i in students:
    print(i[0],"-",i[1])

#Function to give the average
def average_score(students):
    total = 0 
    for name, grade in students:
        total = total + grade
    return total/len(students)

#Function to give the top student
def top_student(students):
    top_name, top_grade = max(students, key=lambda s: s[1])
    return top_name ,top_grade    

#Function to give the failed students
def failed_students(students):
    failed_student = []
    for name, grade in students:
        if grade < 60:
            failed_student.append(name)
    return failed_student    

print("Average score:", average_score(students))

name, grade = top_student(students)
print(f"Top student: {name} ({grade})")

failed = failed_students(students)
print("Failed students:", ", ".join(failed) if failed else "None")





# The same code but without functions


# number = int(input("Enter number of students: "))

# students = []

# for i in range(number):
#     student = input("Enter student " + str(i+1) + " name: ")
        
#     while True:
#         grade = int(input("Enter " + str(student) + "'s score: "))
#         if 0 <= grade <= 100:
#             break
#         else:
#             print("Invalid input")       
#     student_info = (student, grade)
#     students.append((student_info))
                
# print("students =", students)

# print("All students and scores: ")

# for i in students:
#     print(i[0],"-",i[1])

# print("Average score: ", end="")
# total = 0
# for name, grade in students:
#     total += grade

# average = total / len(students)

# print(average)

# top_student = max(students, key=lambda s: s[1])
# print("Top student:", top_student)

# names = []
# for name, grade in students:
#     if grade < 60:
#         names.append(name)

# print("Failed students: ", end="")
# for name in names:
#     print(name, end=", ")
