n=int(input("enter n: "))
i=1
while i<=n:
      j=1
      while j<=i:
            print("*",end="")
            j=j+1
      s=0
      while s<=(n-i)*2:
            print(" ",end="")
            s=s+1
      k=1
      while k<=i:
            print("*",end="")
            k=k+1
      print()
      i=i+1
"""
enter n: 5
*         *
**       **
***     ***
****   ****
***** *****
"""