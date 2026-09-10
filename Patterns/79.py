n=int(input("enter n: "))
i=1
while i<=n:
      j=1
      while j<=i:
            if i==j or j==1:
               print(j,end="")
            else:
               print(" ",end="")
            j=j+1
      print()
      i=i+1
x=n-1
while x>=1:
      y=1
      while y<=x:
            if x==y or y==1:
               print(y,end="")
            else:
               print(" ",end="")
            y=y+1
      print()
      x=x-1
"""
enter n: 5
1
12
1 3
1  4
1   5
1  4
1 3
12
1
"""