# Student-Database-Management-Hashing
The Student Database Management System using Hashing is a Python-based project that uses a hash table to add, search, update, display, and delete student records efficiently.
# Student Database Management System Using Hashing

## 1. Project Description
This is a Python mini project developed for the Data Structures subject. It uses hashing to store, search, update, and delete student records efficiently.

## 2. Objectives
- To understand the concept of hashing.
- To implement a hash table in Python.
- To manage student records using roll numbers.
- To handle collisions using separate chaining.
- To perform insertion, searching, updating, and deletion.

## 3. Technologies Used
- Programming Language: Python
- Data Structure: Hash Table
- Collision Resolution: Separate Chaining

## 4. Features
1. Add student records.
2. Display all student records.
3. Search students by roll number.
4. Update student details.
5. Delete student records.
6. Handle hash collisions.

## 5. Hashing Technique
The hash function used is:

Index = Roll Number % Table Size

The table size is 10. Separate chaining is used to store multiple student records at the same index.

## 6. How to Run
1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Run the command:

   `python student_database.py`

## 7. Time Complexity
- Insertion: O(1) average
- Searching: O(1) average
- Deletion: O(1) average
- Worst case for these operations: O(n)

## 8. Limitations
Student records are stored in memory and are lost when the program exits.

## 9. Conclusion
This project demonstrates how hashing can be used to manage student records. Separate chaining handles collisions and allows multiple records to be stored at the same hash index.

## 10. Author
Your Name
