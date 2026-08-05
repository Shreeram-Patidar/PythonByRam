n=int(input("enter n: "))
i=n
while i>=1:
      s=1
      while s<=n-i:
            print(" ",end="")
            s=s+1
      j=1
      while j<=i*2-1:
            print("*",end="")
            j=j+1
      print()
      i=i-1
"""
enter n: 5
*********
 *******
  *****
   ***
    *
"""