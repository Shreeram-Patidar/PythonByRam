"""
Library Access System
   A library checks:

* If membership is active → Entry allowed
* If books issued < 3 → Can issue more books

Input:
Membership active (yes/no): yes
Books issued: 2

Output:
Entry allowed
Can issue more books
"""

membership=input("Member active(yes or no): ")
book=int(input("enter book issued: "))
if membership=="yes":
    print("Entry allowed")
if book<3:
    print("Can issue more books")