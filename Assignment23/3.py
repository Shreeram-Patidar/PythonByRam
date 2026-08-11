"""
Secure Banking Transaction Analyzer

A banking server generates encrypted transaction IDs using letters and digits.

The fraud detection team wants a Python program to find the first digit that does not repeat in the transaction ID.

If no unique digit exists, print:

text
No unique digit found


### Input:

text
A122334455667789


### Output:

text
1
"""
text=input("Enter text: ")
for ch in text:
    count=text.count(ch)
    if count==1:
       if ch.isdigit():
          print("text")
          print(ch)
          break
else:
   print("No unique digit found")
