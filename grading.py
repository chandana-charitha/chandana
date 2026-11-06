name = input("Enter Student name: ")
marks = int(input("Enter marks: "))
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 35:
    grade = "D"
else:
    grade = "Fail"
print("Student Name:", name)
print("Grade:", grade)