"""
3.Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint:  Delivery was delayed again today

Output:
Total words: 5
"""
s=input("enter complaint: ")
count=0
if s[0]!=" ":
   count+=1 
i=0
while i<len(s):
      if s[i]==" " and s[i-1]!=" ":
         count+=1
      i=i+1
print("Total word: ",count)

