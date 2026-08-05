n=int(input("enter n: "))
i=1
while i<=n:
      s=1
      while s<=i-1:
            print(" ",end="")
            s=s+1
      j=0
      while j<=n-i:
            print(i,end="")
            j=j+1
      print()
      i=i+1
"""
enter n: 5
11111
 2222
  333
   44
    5
"""
