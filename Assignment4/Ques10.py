"""
Question 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4
"""

seconds=int(input("Enter total seconds:"))
hrs=(seconds)//3600
seconds=seconds-hrs*3600
minutes=(seconds)//60
seconds=seconds-minutes*60

print("Hours :",hrs)
print("Minutes:",minutes)
print("Seconds :",seconds)
