n=int(input("enter n: "))
i=1
while i<=n:
      s=1
      while s<=n-i:
            print(" ",end="")
            s=s+1
      j=1
      while j<=i:
            if i==j or j==1 or i==n:
               print("X",end=" ")
            else:
               print("_",end=" ")
            j=j+1
      print()
      i=i+1
"""
enter n: 5
    X
   X X
  X _ X
 X _ _ X
X X X X X
"""
