import math
n=int(input("enter n: "))
i=0
while i<n:
      s=1
      while s<=n-i:
            print(" ",end="")
            s=s+1
      j=0
      while j<=i:
            num=int(math.factorial(i)/(math.factorial(j)*math.factorial(i-j)))
            print(num,end=" ")
            j=j+1
      print()
      i=i+1
"""
enter n: 5
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
"""
      