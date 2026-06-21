"""
========================================
Question 4: Travel Fare Calculator
========================================

A cab company charges ₹15 per kilometer.

Write a Python program that:
- Accepts the number of kilometers traveled.
- Calculates the total fare.
- Displays the result.

Example:
Distance = 20 km
Total fare = ₹300

"""

total_amount=int(input("enter toal amount of cart:"))
gst=total_amount*12/100
print("total amount to pay as gst 12%:",gst)
total = total_amount+gst
print("total amount of pay :",total)
