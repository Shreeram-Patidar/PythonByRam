n=int(input("enter n: "))
i=n
while i>=1:
      s=1
      while s<=n-i:
            print(" ",end="")
            s=s+1
      j=1
      while j<=i:
            print(i,end="")
            j=j+1
      print()
      i=i-1
"""
enter n: 5
55555
 4444
  333
   22
    1
"""