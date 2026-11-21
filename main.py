students = []
def calculate_average(grade1, grade2, grade3):
    return (grade2 + grade2 + grade3) /3
def add_student():
    name = input("Enter student name: ")
    grade1 = float(input("Enter grade 1: "))
    grade2 = float(input("Enter grade 2: "))
    grade3 = float(input("Enter grade 3: "))

    average = calculate_average(grade1, grade2, grade3)

    students.append([name, grade1, grade2, grade3, average])

    print("Student added successfully!")
    print("Average:", average)

add_student()
