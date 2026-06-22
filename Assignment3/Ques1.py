"""
Question 1: Speed Calculator

Write a Python program that:

Accepts distance (in km) and time (in hours).
Calculates speed.

Input:
Distance = 120
Time = 2

Output:
Speed = 60 km/h
"""

distance=int(input("Enter the distance: "))
time=int(input("Enter the time: "))
speed=distance/time
print("Speed =",speed,"km/h")
