"""=====================================================================
QUESTION 2: STUDENT RESULT PROCESSING
=====================================

A training institute wants to manage student records using NamedTuple.

Fields:
roll_no, name, course, marks

Requirements:

1. Read N student records from the user and store them in a list of NamedTuples.

---

2. Display all student details.

---

3. Find and display the topper of the class.

---

4. Count and display the number of students scoring above 80 marks.

---

5. Calculate and display the average marks.

---

6. Accept a course name from the user and display all students enrolled in that course.

---

Test Case:

Input:
Enter number of students: 4

1 Ravi Python 85
2 Anjali Java 78
3 Karan Python 92
4 Pooja Testing 88

Enter course: Python

Expected Output:
Topper:
3 Karan Python 92

Students Above 80:
3

Average Marks:
85.75

Students in Python Course:
1 Ravi Python 85
3 Karan Python 92
"""

from typing import NamedTuple


# Define NamedTuple
class Student(NamedTuple):
    roll_no: int
    name: str
    course: str
    marks: int


# 1. Read N student records
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    data = input().split()

    roll_no = int(data[0])
    name = data[1]
    course = data[2]
    marks = int(data[3])

    student = Student(roll_no, name, course, marks)
    students.append(student)


# 2. Display all student details
print("\nAll Student Details:")

for student in students:
    print(student.roll_no, student.name,
          student.course, student.marks)


# 3. Find the topper
topper = students[0]

for student in students:
    if student.marks > topper.marks:
        topper = student

print("\nTopper:")
print(topper.roll_no, topper.name,
      topper.course, topper.marks)


# 4. Count students scoring above 80
count = 0

for student in students:
    if student.marks > 80:
        count = count + 1

print("\nStudents Above 80:")
print(count)


# 5. Calculate average marks
total = 0

for student in students:
    total = total + student.marks

average = total / n

print("\nAverage Marks:")
print(average)


# 6. Display students by course
course_name = input("\nEnter course: ")

print("\nStudents in", course_name, "Course:")

for student in students:
    if student.course == course_name:
        print(student.roll_no, student.name,
              student.course, student.marks)