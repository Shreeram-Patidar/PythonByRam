n=int(input("enter n: "))
i=1
while i<=n:
      s=1
      while s<=n-i:
            print(" ",end="")
            s=s+1
      j=1
      while j<=i:
            print(i,end="")
            j=j+1
      print()
      i=i+1
"""
enter n: 5
    1
   22
  333
 4444
55555
"""