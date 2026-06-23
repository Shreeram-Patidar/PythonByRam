"""
Question 3: Student Marks Analysis

A student wants to calculate total marks, average, and percentage from 5 subjects.

Input:
Marks = 78, 85, 90, 88, 80

Expected Output:
Total = 421
Average = 84.2
Percentage = 84.2
"""

a,b,c,d,e=map(int,input("Enter marks ").split())
total=a+b+c+d+e
avg=total/5
print("Total :",total)
print("Average marks is :",avg)
percentage=(avg/100)*100
print("percentage is :",percentage,"%")
