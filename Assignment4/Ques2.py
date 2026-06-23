"""
Question 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0
"""

mobile_price=int(input("Mobile price="))
down_pay=int(input("Down payment ="))
interest_rate=int(input("Interest rate ="))
months=int(input("Months ="))
remaining=(mobile_price)-(down_pay)
interest=remaining*(interest_rate/100)
print("Remaining Amount :",remaining)
print("Total with Interest :",remaining+interest)
monthly_emi=remaining/months
print("Monthly EMI :",monthly_emi)



