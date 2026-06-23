"""
Question 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75
"""

total_bill=float(input("Total bill amount ="))
gst=int(input("GST ="))
service_charge=int(input("Service Charge ="))
friend=int(input("Number of friends ="))
final=total_bill+(total_bill*(5/100))+(total_bill*(10/100))
print("Final Bill =",final)
print("Each Person Pays =",final/friend)

