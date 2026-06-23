"""
Question 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km
"""

hrs,minutes=map(int,input("enter your time in hrs and minutes").split())
speed = float(input("Enter Speed in km/h"))
minutes=minutes/60
time=float(hrs+minutes)
dist = speed*time
print("Distance Travelled :",dist)
print("Time in hours :",time)
