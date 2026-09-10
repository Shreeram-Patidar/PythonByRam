n=int(input("enter n: "))
i=1
while i<=n:
      j=0
      while j<=n-i:
            print("*",end="")
            j=j+1
      s=1
      while s<=i*2-1:
            print(" ",end="")
            s=s+1
      k=n
      while k>=i:
            print("*",end="")
            k=k-1
      print()
      i=i+1
"""
enter n: 5
***** *****
****   ****
***     ***
**       **
*         *
"""