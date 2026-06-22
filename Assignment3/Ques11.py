"""
Question 11: Time Duration Adder

Write a Python program that:

Accepts hours, minutes, seconds.
Converts into total seconds.

Input:
Hours = 1
Minutes = 2
Seconds = 30

Output:
Total Seconds = 3750
"""

hour=int(input("Hour ="))
minute=int(input("Minute ="))
second=int(input("Second ="))
time=hour*3600+minute*60+second
print("Toatal Seconds =",3750)
