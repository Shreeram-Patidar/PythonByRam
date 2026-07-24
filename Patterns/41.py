n=int(input("enter n: "))
i=1
ch=65
while i<=n:
      j=1
      while j<=i*2-1:
            print(chr(ch),end="")
            j=j+1
            ch=ch+1
      print()
      i=i+1 
"""
enter n: 5
A
BCD
EFGHI
JKLMNOP
QRSTUVWXY
"""