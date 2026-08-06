"""
Find the First Non-Repeated Character

Railway Ticket Fraud Detection System

The railway department generates ticket reference IDs automatically.

Sometimes, due to technical issues, many characters get repeated inside the ticket ID.

The department wants a Python program that finds the first character that appears only once in the string.

Example 1

Input:
aabbccddefg
Output:
e

"""

s=input("Enter string: ")
i=0
while i<len(s):
      ch=s[i]
      count=0
      j=0
      while j<len(s):
          if s[j]==ch:
             count+=1
          j=j+1
      if count==1:
         print(ch)
         break
      i=i+1


          


