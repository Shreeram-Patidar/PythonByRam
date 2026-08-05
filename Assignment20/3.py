"""
Smart Chat Message Cleaner

A social media company noticed that users often enter messages with
unnecessary spaces. To improve readability and storage efficiency, the
system should remove extra spaces and keep only a single space between
words.

Input: Enter message: Java is easy

Output: Cleaned Message: Java is easy
"""
s=input("Enter message: ")
r=""
i=0
while i<len(s):
      if s[i]==" " and s[i-1]==" ":
         pass
      else:
        r=r+s[i]
      i=i+1
print(r)