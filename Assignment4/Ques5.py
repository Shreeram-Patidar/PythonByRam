"""
Question 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5
"""

salary=int(input("Monthly salary ="))
days=int(input("Working days ="))
hour=int(input("Working hour per day ="))
per_day=salary/days
per_hour=per_day/8

print("Salary per Day :",per_day)
print("Salary per hours :",per_hour)
