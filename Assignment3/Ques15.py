"""
Question 15: Average Speed for Multiple Trips

Write a Python program that:

Accepts distance1, time1, distance2, time2.
Calculates average speed.

Input:
Distance1 = 60
Time1 = 1
Distance2 = 40
Time2 = 1

Output:
Average Speed = 50 km/h
"""

distance1=int(input("Enter the first distance :"))
time1=int(input("Enter the first time"))
distance2=int(input("Enter the second distance :"))
time2=int(input("Enter the second time"))
avg_speed=(distance1+distance2)/(time1+time2)
print("Average Speed =",avg_speed)
