grades = {"Precious": 85,"Joshua": 90,"Obinna": 78}
name = input("Enter student name: ")
if name in grades:
    print(f"{name}`s grade: {grades[name]}")
else:
    print("Student not found")