n=int(input("enter n: "))
i=n
while i>=1:
   j=1
   ch=65
   while j<=i:
      print(chr(ch),end="")
      j=j+1
      ch=ch+1
   print()
   i=i-1
"""
enter n: 5
ABCDE
ABCD
ABC
AB
A
"""