"""
Question 8: Compound Interest

A person invests money in a bank that provides compound interest annually.

Input:
Principal = 10000
Rate = 5%
Time = 2 years

Expected Output:
Amount after interest = 11025.0
"""

p,r,t,=map(int,input("enter principle rate or time").split())
total_amount=p*(1+r/100)**t
print("Total amount :",total_amount)
