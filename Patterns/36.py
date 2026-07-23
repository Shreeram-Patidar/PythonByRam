n=int(input("enter n: "))
i=n
while i>=1:
   j=1
   ch=65
   while j<=i:
      if j==i or j==1 or i==n:
         print(chr(ch),end="")
      else:
         print(" ",end="")
      j=j+1
      ch=ch+1
   print()
   i=i-1
"""
enter n: 5
ABCDE
A  D
A C
AB
A
"""