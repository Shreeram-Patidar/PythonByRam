"""
Social Media Hashtag Trend Window

A social media company wants to analyze the smallest substring containing all unique characters from a hashtag.

### Input:

text
aabcbcdbca


### Output:

text
dbca


### Explanation:

dbca contains all unique characters: a,b,c,d
"""
text=input("Enter text: ")
visit=""
max=0
long=""
for ch in text:
    if ch not in visit:
       visit+=ch
    else:
       if len(visit)>max:
          max=len(visit)
          long=visit
          visit=visit[1:]
print(long)
       

