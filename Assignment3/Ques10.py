"""
Question 10: Percentage Calculator

Write a Python program that:

Accepts total marks and obtained marks.
Calculates percentage.

Input:
Total = 500
Obtained = 400

Output:
Percentage = 80%
"""

total_marks=int(input("Enter Total Marks :"))
obtain_marks=int(input("Enter Obtained Marks :"))
percentage=(obtain_marks/total_marks)*100
print("Percentage =",percentage,"%")
