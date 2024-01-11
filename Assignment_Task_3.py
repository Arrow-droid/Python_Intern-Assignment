"""
Task 3: MySQL Database Operations with Python ( Compulsory )
Problem Statement:
Your task is to write a Python program that accomplishes the following:
First create a database , table and add these column ‘student_id’, ‘first_name’, ‘last_name’,
‘age’, ‘grade’.
Connects to your MySQL database with python.
Inserts a new student record into the "students" table with the following details:
First Name: "Alice"
Last Name: "Smith"
Age: 18
Grade: 95.5
Updates the grade of the student with the first name "Alice" to 97.0.
Deletes the student with the last name "Smith."
Fetches and displays all student records from the "students" table.
"""

# pip install mysql-connector-python

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="ashutosh",
    password="password",
    database="mydb"
)

# Create a cursor object
cursor = mydb.cursor()

# Create a 'students' table
cursor.execute("""
    students (student_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        age INT,
        grade FLOAT)""")

# Insert a new student record
cursor.execute("""
    INSERT INTO students (first_name, last_name, age, grade)
    VALUES (%s, %s, %s, %s)
""", ("Alice", "Smith", 18, 95.5))

mydb.commit()

# Update the grade of the student with the first name "Alice"
cursor.execute("""
    UPDATE students
    SET grade = %s
    WHERE first_name = %s
""", (97.0, "Alice"))

mydb.commit()

# Delete the student with the last name "Smith"
cursor.execute("""
    DELETE FROM students
    WHERE last_name = %s
""", ("Smith",))

mydb.commit()
# Fetch and display all student records
cursor.execute("SELECT * FROM students")
students = cursor.fetchall()

for student in students:
    print(student)

# Commit changes and close the connection
mydb.commit()
mydb.close()
