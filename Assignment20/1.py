"""
Bank Customer Account Privacy System

A national bank is developing a secure customer portal where account
numbers should not be displayed completely on the screen. For security
reasons, the system should hide all digits except the last four digits
before showing them to users.

Conditions: - Display only the last 4 digits - Replace all previous
characters with *

Input: Enter account number: 123456789012

Output: Masked Account: ****9012
"""
account=input("Enter account number: ")
masked=""

i=0
while i<len(account)-4:
      masked=masked+"*"
      i=i+1

i=len(account)-4
while i<len(account):
      masked=masked+account[i]
      i=i+1

print(masked)
