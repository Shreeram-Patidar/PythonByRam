"""
7.Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number
"""
s=input("Enter vehicle number: ")
if len(s)==10 and s[:2].isalpha() and s[2:4].isdigit() and s[4:6].isalpha() and s[6:].isdigit():
   print("Valid Vehicle Number")
else:
   print("Invalid Vehicle Number")