"""
College Result Processing System


A college wants to generate grades for students automatically based on their marks in an exam. The grading criteria are as follows:

* 90 and above → Grade A
* 75 to 89 → Grade B
* 60 to 74 → Grade C
* 50 to 59 → Grade D
* Below 50 → Fail

Write a Python program to display the grade of a student.

Input:
Enter marks: 67

Output:
Grade: C
"""

mark=int(input("Enter your Marks: "))

if mark>=90:
    print("Grade A")
elif mark>=75:
    print("Grade B")
elif mark>=60:
    print("Grade C")
elif mark>=50:
    print("Grade D")
else:
    print("Fail")