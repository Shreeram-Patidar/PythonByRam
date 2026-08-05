"""
Advanced Student Registration Data Processing System

A national university is developing an intelligent registration portal.
Students enter registration codes using uppercase letters, lowercase
letters, digits, and special symbols. Due to inconsistent data entry,
the administration wants the system to standardize and process the
information before storing it.

Conditions: - Ignore all special characters (@ # $ % & * - _) - Separate
alphabets and digits - Convert all alphabets to lowercase - Remove
duplicate alphabets - Arrange alphabets in ascending order - Arrange
digits in descending order - Display alphabets first and digits later -
If no digits are found, display “No Digits Found”

Test Case 1 Input: Enter registration code: zBc@638

Output: Result: bcz863

Test Case 2 Input: Enter registration code: 5Br$dE654b

Output: Result: bder6554

Test Case 3 Input: Enter registration code: A9@C3d#6B1a

Output: Result: abcd9631

Test Case 4 Input: Enter registration code: X#X@M2A4x7

Output: Result: amx742

Test Case 5 Input: Enter registration code: r@T#y

Output: Result: rty No Digits Found
"""
code=input("Enter registration code: ")
alpha=""
digit=""
i=0
while i<len(code):
     if (code[i]>="a" and code[i]<="z") or (code[i]>="A" and code[i]<="Z"):
        alpha+=code[i]
     elif code[i]>="0" and code[i]<="9":
        digit+=code[i]
     i=i+1
print(alpha)
print(digit)
al=""
i=0
while i<len(alpha):
      if alpha[i]>="A" and alpha[i]<="Z":
         al=al+chr(ord(alpha[i])+32)
      else:
         al=al+alpha[i]
      i=i+1
print(al)
a=""
visited=""
i=0
while i<len(al):
      if al[i] in visited:
         pass
      else:
         visited+=al[i]
         a+=al[i]
      i+=1
print(a)
a="".join(sorted(a))
print(a)
digit="".join(sorted(digit))
d=digit[::-1]
print(d)
result=""
result=a+d
print(result)
if d=="":
   print("No Digit")