n=int(input("enter n: "))
i=1
while i<=n:
      j=1
      while j<=n:
            if i==1 or i==n or j==1 or j==n or i==j or j==n-i:
               print(".",end="")
            else:
               print(" ",end="")
            j=j+1
      print()
      i=i+1
"""
..........
..     . .
. .   .  .
.  . .   .
.   .    .
.  . .   .
. .   .  .
..     . .
.       ..
..........
"""
     