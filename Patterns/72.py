n=int(input("enter n: "))
i=n
while i>=1:
      ch=65
      s=1
      while s<=n-i:
            print(" ",end="")
            s=s+1
      j=1
      while j<=i:
            print(chr(ch),end=" ")
            j=j+1
            ch=ch+1
      print()
      i=i-1
"""
enter n: 5
A B C D E
 A B C D
  A B C
   A B
    A
"""