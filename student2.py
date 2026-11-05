# Read name, USN, 3 courses, and 3 marks

print("Enter a student name,USN,3 courses,3 marks")
name = input("Enter the name:")
USN = input("Enter the USN:")

#total_course = int(input("Enter the total_course"))
course1 = int(input("Enter the course name:"))
course2 = int(input("Enter the course name:"))
course3 = int(input("Enter the course name:"))
marks1 = int(input("Enter the marks:"))
marks2 = int(input("Enter the marks:"))
marks3 = int(input("Enter the marks:"))

#calculate total and average
total = marks1+marks2+marks3
average= (total/3)

#display in the format

print("*" * 50)
print(f"Name is {name}")
print("*" * 50)
print(f"USN is {USN}")
print("*" * 50)
print("COURSES\t\tMARKS")
print("*" * 50)
print(f"{course1}\t\t{marks1}")
print(f"{course2}\t\t{marks2}")
print(f"{course3}\t\t{marks3}")
print("*" * 50)
print(f"TOTAL\t\t{total}")
print(f"AVERAGE\t\t{average}")
print("*" * 50)





