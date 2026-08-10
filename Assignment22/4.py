"""
Find All Characters with Maximum Frequency
Website Traffic Analysis System

A web analytics company tracks user activity symbols in server logs.

The company wants to identify all characters having the maximum frequency in the given string.

Input:
aabbbccddd
Output:
b d
"""
s = input("Enter String: ")
max=0
count=0
for ch in s:
    count=s.count(ch)
    if count>max:
       max=count
visited=""
i=0
while i<len(s):
   ch=s[i]
   if s.count(ch)==max:
      if ch not in visited:
         visited+=ch
         print(ch,end=" ")
   i=i+1
