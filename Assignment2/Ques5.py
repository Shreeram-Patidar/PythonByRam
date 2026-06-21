"""
========================================
Question 5: Shopping Tax Calculator
========================================

Your shopping cart total doesn’t include tax. A 12% GST is applied.

Write a Python program that:
- Accepts the cart total amount.
- Calculates 12% tax.
- Displays the tax and final total amount.

Example:
Cart = ₹2000
Tax = ₹240
Total = ₹2240

"""

total=int(input("enter total amount:"))
inr10 = total//10
total = total - inr10*10
inr5 = total//5
print("TOTAL AMOUNT IS :",amount)
print("In INR10 is : ",inr10,"*",10,"=",inr10*10)
print("In INR15 is : ",inr5,"*",5,"=",inr5*5)
