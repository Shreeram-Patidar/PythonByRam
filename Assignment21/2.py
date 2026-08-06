"""
Reverse Sentence + Reverse Each Word

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.
Input:

Python is powerful

Output:

lufrewop si nohtyP

"""

s=input("Enter message: ")
s=s.split(" ")
s=s[::-1]
rev=""
i=0
while i<len(s):
      ch=s[i]
      rev=rev+ch[::-1]+" "
      i=i+1
s=rev
print(s)
      