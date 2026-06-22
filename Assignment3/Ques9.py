"""
Question 9: Fuel Cost Calculator

Write a Python program that:

Accepts distance (km), mileage (km/litre), and petrol price.
Calculates total fuel cost.

Input:
Distance = 100
Mileage = 20
Petrol Price = 100

Output:
Cost = 500
"""

distance=int(input("Enter Distance :"))
mileage=float(input("Enter Mileage :"))
petrolprice=float(input("Enter Petrol Price :"))
fuel=distance/mileage
cost=fuel*petrolprice
print("Cost =",cost)
