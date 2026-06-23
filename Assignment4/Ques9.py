"""
Question 9: Petrol Cost Calculation

You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.

Input:
Distance = 450 km
Mileage = 15 km/litre
Petrol price = 110/litre

Expected Output:
Petrol Used = 30.0 litres
Total Cost = 3300.0
"""

d,m,p=map(int,input("Enter distance mileage petrol price").split())
petrol_used = d/m
total_cost = petrol_used*p
print("petrol used: ",petrol_used)
print("Total Cost :",total_cost)
