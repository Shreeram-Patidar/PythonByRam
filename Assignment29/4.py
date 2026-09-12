"""=====================================================================
QUESTION 4: ONLINE SHOPPING ORDERS
==================================

An online shopping company stores customer orders using NamedTuple.

Fields:
order_id, customer_name, product_name, amount

Requirements:

1. Read N order records from the user and store them in a list of NamedTuples.

---

2. Display all order details.

---

3. Find and display the order having the highest amount.

---

4. Calculate and display total sales.

---

5. Count the number of orders whose amount is greater than ₹10,000.

---

Test Case:

Input:
Enter number of orders: 5

O101 Rahul Laptop 55000
O102 Priya Mouse 800
O103 Amit Mobile 25000
O104 Neha Keyboard 1500
O105 Rakesh TV 45000

Expected Output:
Highest Value Order:
O101 Rahul Laptop 55000

Total Sales:
127300

Orders Above ₹10,000:
3
"""

from typing import NamedTuple


# Define NamedTuple
class Order(NamedTuple):
    order_id: str
    customer_name: str
    product_name: str
    amount: int


# 1. Read N order records
orders = []

n = int(input("Enter number of orders: "))

for i in range(n):
    data = input().split()

    order_id = data[0]
    customer_name = data[1]
    product_name = data[2]
    amount = int(data[3])

    order = Order(order_id, customer_name, product_name, amount)
    orders.append(order)


# 2. Display all order details
print("\nAll Order Details:")

for order in orders:
    print(order.order_id, order.customer_name,
          order.product_name, order.amount)


# 3. Find order with highest amount
highest = orders[0]

for order in orders:
    if order.amount > highest.amount:
        highest = order

print("\nHighest Value Order:")
print(highest.order_id, highest.customer_name,
      highest.product_name, highest.amount)


# 4. Calculate total sales
total_sales = 0

for order in orders:
    total_sales = total_sales + order.amount

print("\nTotal Sales:")
print(total_sales)


# 5. Count orders above ₹10,000
count = 0

for order in orders:
    if order.amount > 10000:
        count = count + 1

print("\nOrders Above ₹10,000:")
print(count)