"""
Replace Consecutive Duplicate Characters with Single Character
Data Compression System

A cloud storage company wants to reduce unnecessary repeated characters in text logs.

Write a Python program that replaces consecutive duplicate characters with a single occurrence.

Input:
aaabbbccccdddaa
Output:
abcda
"""
s = input("Enter Text: ")
new=""
new=new+s[0]
i=1
while i<len(s):
   ch=s[i]
   if s[i]!=s[i-1]:
      new+=ch
   i+=1
print(new)