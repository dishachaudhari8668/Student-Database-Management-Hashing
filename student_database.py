
# Student Database Management System Using Hashing

SIZE = 10
hash_table = [[] for _ in range(SIZE)]


# Hash function
def hash_function(roll_no):
    return roll_no % SIZE


# Add student
def add_student():
    roll_no = int(input("Enter roll number: "))
    index = hash_function(roll_no)

    for student in hash_table[index]:
        if student["roll_no"] == roll_no:
            print("Student already exists!")
            return

    name = input("Enter student name: ")
    course = input("Enter course: ")
    marks = float(input("Enter marks: "))

    student = {
        "roll_no": roll_no,
        "name": name,
        "course": course,
        "marks": marks
    }

    hash_table[index].append(student)
    print("Student added successfully!")


# Display all students
def display_students():
    found = False

    print("\n--- Student Records ---")

    for bucket in hash_table:
        for student in bucket:
            print("Roll No:", student["roll_no"])
            print("Name:", student["name"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])
            print("----------------------")
            found = True

    if not found:
        print("No student records found.")


# Search student
def search_student():
    roll_no = int(input("Enter roll number to search: "))
    index = hash_function(roll_no)

    for student in hash_table[index]:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            print("Roll No:", student["roll_no"])
            print("Name:", student["name"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])
            return

    print("Student not found!")


# Update student
def update_student():
    roll_no = int(input("Enter roll number to update: "))
    index = hash_function(roll_no)

    for student in hash_table[index]:
        if student["roll_no"] == roll_no:
            student["name"] = input("Enter new name: ")
            student["course"] = input("Enter new course: ")
            student["marks"] = float(input("Enter new marks: "))
            print("Student updated successfully!")
            return

    print("Student not found!")


# Delete student
def delete_student():
    roll_no = int(input("Enter roll number to delete: "))
    index = hash_function(roll_no)

    for student in hash_table[index]:
        if student["roll_no"] == roll_no:
            hash_table[index].remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found!")


# Main menu
while True:
    print("\n===== STUDENT DATABASE MANAGEMENT =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Thank you for using Student Database!")
            break
        else:
            print("Invalid choice. Please try again.")

    except ValueError:
        print("Invalid input! Enter numbers correctly.")
