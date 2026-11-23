 
import json

students = []

 
def calculate_average(grade1, grade2, grade3):
    return (grade1 + grade2 + grade3) / 3


def get_grade(number):
    while True:
        try:
            grade = float(input(f"Enter grade {number}: "))

            if 0 <= grade <= 100:
                return grade
            else:
                print("Invalid grade! Enter a grade between 0 and 100.")

        except ValueError:
             print("Please enter a valid number.")


def save_students(): 
    with open("students.json", "w") as file: 
        json.dump(students, file, indent=4)


def load_students():
    try:
        with open("students.json", "r") as file: 
            students.extend(json.load(file))
    except FileNotFoundError:
        pass


def add_student():
    name = input("Enter student name: ")

    grade1 = get_grade(1)
    grade2 = get_grade(2)
    grade3 = get_grade(3)

    average = calculate_average(grade1, grade2, grade3)

    students.append([name, grade1, grade2, grade3, average])

    save_students()

    print("Student added successfully!")
    print(f"Average: {average:.2f}")


def display_students():
    if not students:
        print("No students found.")
        return

    print("\n--- Students List ---")

    for student in students:
        name, g1, g2, g3, avg = student

        status = "PASS" if avg >= 50 else "FAIL"

        print(
            f"Name: {name} | Grades: {g1}, {g2}, {g3} "
            f"| Average: {avg:.2f} | Status: {status}"
        )


def search_student():
    name = input("Enter student name to search: ")

    for student in students:
        if student[0].lower() == name.lower():
            status = "PASS" if student[4] >= 50 else "FAIL"

            print("Student found!")
            print(f"Name: {student[0]}")
            print(f"Grades: {student[1]}, {student[2]}, {student[3]}")
            print(f"Average: {student[4]:.2f}")
            print(f"Status: {status}")
            return

    print("Student not found.")


def delete_student():
    name = input("Enter student name to delete: ")

    for student in students:
        if student[0].lower() == name.lower():
            students.remove(student)
            save_students()
            print("Student deleted successfully!")
            return

    print("Student not found.")


load_students()

while True:
    print("\n===== Student Management Systrm =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
