"""
1.Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username
"""
s=input("Enter username: ")
valid=0
if (s[0]>='a' and s[0]<='z') or (s[0]>='A' and s[0]<='Z'):
   valid=1
digit=0
score=0
space=0
i=1
while i<len(s):
      ch=s[i]
      if ch>="0" and ch<="9":
         digit=1
      elif ch=="_":
         score=1
      elif ch==" ":
         space=1
      i=i+1
if len(s)>=5 and len(s)<=12 and valid==1 and digit==1 and score==1 and space==0:
   print("Valid Username")
else:
   print("Invalid Username")