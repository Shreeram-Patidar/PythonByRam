"""
Employee Short ID Generator

A multinational company wants to automatically generate short IDs for
employees while creating official email accounts. The system should take
the employee’s full name and create an ID using the first character of
each word.

Conditions: - Take first character of every word - Convert all
characters to uppercase

Input: Enter employee name: ajay singh thakur
Output: Employee Short ID: AST
"""
s=input("Enter employee name: ")
r=""
if s[0]>="a" and s[0]<="z":
   r=r+chr(ord(s[0])-32)
i=1
while i<len(s):
      if s[i]!=" " and s[i-1]==" ":
         if s[i]>='a' and s[i]<='z':
            r=r+chr(ord(s[i])-32)
      i=i+1
print(r)
      