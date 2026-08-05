"""
Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop
"""
message=input("Enter message: ")
words=message.split()
print(words)
rev=""
for word in words:
    rev=rev+word[::-1]+" "
print(rev)
         