"""
=====================================================================
QUESTION 1: EMPLOYEE SALARY ANALYSIS
====================================

A company wants to store employee details and generate salary reports using NamedTuple.

Fields:
emp_id, emp_name, department, salary

Requirements:

1. Read N employee details from the user and store them in a list of NamedTuples.

---

2. Display all employee details.

---

3. Find and display the employee with the highest salary.

---

4. Find and display the employee with the lowest salary.

---

5. Calculate and display the average salary of all employees.

---

6. Accept a department name from the user and display all employees belonging to that department.

---

Test Case:

Input:
Enter number of employees: 4

101 Rahul IT 50000
102 Priya HR 45000
103 Amit IT 70000
104 Neha Finance 60000

Enter department: IT

Expected Output:
Highest Salary Employee:
103 Amit IT 70000

Lowest Salary Employee:
102 Priya HR 45000

Average Salary:
56250.0

Employees in IT Department:
101 Rahul IT 50000
103 Amit IT 70000
"""

from typing import NamedTuple

# Define NamedTuple
class Employee(NamedTuple):
      emp_id: int
      emp_name: str
      department: str
      salary: int

# 1. Read N employee details
employees=[]

n=int(input("enter number of employees: "))

for i in range(n):
    data=input().split()

    emp_id=int(data[0])
    emp_name=data[1]
    department=data[2]
    salary=int(data[3])

    emp=Employee(emp_id, emp_name, department, salary)
    employees.append(emp)

# 2. Display all employee details
print("\nAll Employee Details:")

for emp in employees:
    print(emp.emp_id, emp.emp_name, emp.department, emp.salary)

# 3. Find employee with highest salary
highest = employees[0]

for emp in employees:
    if emp.salary>highest.salary:
       highest=emp

print("\nHighest Salary Employee: ")
print(highest.emp_id, highest.emp_name, highest.department, highest.salary)

# 4. Find employee with lowest salary
lowest = employees[0]

for emp in employees:
    if emp.salary<lowest.salary:
       lowest=emp

print("\nLowest Salary Employee:")
print(lowest.emp_id, lowest.emp_name, lowest.department, lowest.salary)

# 5. Calculate average salary
total = 0

for emp in employees:
    total=total+emp.salary

average=total/n

print("\nAverage Salary:")
print(average)

# 6. Find employees by department
dept = input("\nEnter department: ")

print("\nEmployees in",dept,"Department:")

for emp in employees:
    if emp.department==dept:
       print(emp.emp_id, emp.emp_name, emp.department, emp.salary)
    