n=int(input("enter n: "))
i=1
ch=97
while i<=n:
   j=1
   while j<=i:
      if j==i or j==1 or i==n:
         print(chr(ch),end="")
      else:
         print(" ",end="")
      j=j+1
      ch=ch+1
   print()
   i=i+1
"""
enter n: 5
a
bc
d f
g  j
klmno
"""