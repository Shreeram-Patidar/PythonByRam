"""
3.Character Occurrence Checker in Product Review

An e-commerce website wants to know how many times a particular character appears in a product review.

Input: Enter product review: this product is really good Enter character to check: o

Output: Character 'o' occurs: 3 times
"""
s=input("Enter product review: ")
count=0
for ch in s:
    if ch=='o':
       count=count+1
print("Character 'o' occurs: ",count)
