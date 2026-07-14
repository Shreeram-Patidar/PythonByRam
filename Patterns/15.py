n=int(input("enter n: "))
i=1
ch=65
while i<=n:
   j=1
   while j<=i:
      print(chr(ch),end="")
      j=j+1
   print()
   i=i+1
   ch=ch+1
"""
enter n: 5
A
BB
CCC
DDDD
EEEEE
"""