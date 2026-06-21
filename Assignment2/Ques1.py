"""
========================================
Question 1: Time Converter
========================================

An event management company is developing a scheduling system. One of the key tasks is converting the duration of events from total seconds (which their sensor system records) into a more human-readable format of hours, minutes, and seconds.

Write a Python program that:
- Accepts the total event duration in seconds as input.
- Calculates how many hours, minutes, and seconds it corresponds to.
- Displays the output in the format:
  Hours: x, Minutes: y, Seconds: z

Sample Input:
Total event duration in seconds: 3672

Sample Output:
Hours: 1, Minutes: 1, Seconds: 12
"""

total=int(input("Enter the event duration: "))
hour=total//3600
total=total%3600
minut=total//60
total=total%60
second=total
print(hour,":hour",minut,":minute",second,":second")
