students = [] 
def calculate_average(grade1, grade2, grade3):
    return (grade1 + grade2 + grade3) / 3

def add_student():
    name = input("Enter student name: ")
    grade1 = float(input("Enter grade 1: "))
    grade2 = float(input("Enter grade 2: "))
    grade3 = float(input("Enter grade 3: "))

    average = calculate_average(grade1, grade2, grade3)
    students.append([name, grade1, grade2, grade3, average])

    print("Student added successfully!")
    print(f"Average: {average:.2f}")

def display_students():
    if not students:
        print("No students found.")
        return

    print("\n--- Students List ---")
    for student in students:
         name, g1, g2, g3, avg = student 
         print(f"Name: {name} | Grades: {g1}, {g2}, {g3} | Average: {avg:.2f}")

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Exit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
