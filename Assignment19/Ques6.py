"""
6.Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching
"""
n1=input("Enter first product code: ").lower()
n2=input("Enter Second product code: ").lower()
a=""
b=""
for i in n1:
    if i==" ":
       pass
    else:
       a=a+i
for j in n2:
    if j==" ":
       pass
    else:
       b=b+j
a=a.sorted()
b=b.sorted()
if a==b:
   print("Same")
else:
   print("Not Same")
         


   
                
