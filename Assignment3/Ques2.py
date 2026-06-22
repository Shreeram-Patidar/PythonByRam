"""
Question 2: Salary Calculator

Write a Python program that:

Accepts daily wage and number of days.
Calculates total salary.

Input:
Daily wage = 500
Days = 26

Output:
Salary = 13000
"""

wage=int(input("Enter daily wage: "))
day=int(input("Enter the day: "))
salary=wage*day
print("Salary =",salary)
