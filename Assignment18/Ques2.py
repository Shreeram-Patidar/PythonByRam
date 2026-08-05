"""
2.Space Counter in Chat Messages

A chat application wants to calculate how many spaces are used in a message.

Input: Enter chat message: Good morning everyone how are you

Output: Total spaces: 5
"""
s=input("Enter chat message: ")
space=0
for ch in s:
    if ch==" ":
       space+=1
print("Total space: ",space)