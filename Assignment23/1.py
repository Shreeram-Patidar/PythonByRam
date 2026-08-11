"""
Smart Log File Error Pattern Detector

A cybersecurity company stores server logs containing repeated system activity characters.

To detect suspicious looping behavior, the analytics team wants a Python program that finds the longest repeating substring present in the log file.

If multiple substrings have the same length, print the first one found.

 Input:

text
abcabcbb


Output:

text
abc

"""

s=input("Enter text: ")
sub=""
visited=[]
i=0
while i<len(s):
      if s[i] not in sub:
         sub+=s[i]
      else:
         visited.append(sub)
         sub=""
      i=i+1
max=0
longest=0
i=0
while i<len(visited):
      sub=visited[i]
      if len(sub)>max:
         max=len(sub)
         longest=sub
      i=i+1
print(longest)
    


         
