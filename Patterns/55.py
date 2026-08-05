n=int(input("enter n: "))
i=n
while i>=1:
      s=1
      ch=65
      while s<=n-i:
            print(" ",end="")
            s=s+1
      j=1
      while j<=i:
            print(chr(ch),end="")
            ch=ch+1
            j=j+1
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