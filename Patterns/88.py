n=int(input("enter n: "))
i=1
while i<=n:
      j=1
      while j<=n:
            if i==n:
               print(j,end="")
            elif j==n:
               print(i,end="")
            else:
               print(" ",end="")
            j=j+1
      k=n-1
      while k>=1:
            if i==n:
               print(k,end="")
            else:
               print(" ",end="")
            k=k-1
      print()
      i=i+1
x=n-1
while x>=1:
      y=1
      while y<=n:
            if y==n:
               print(x,end="")
            else:
               print(" ",end="")
            y=y+1
      print()
      x=x-1
"""
enter n: 5
    1
    2
    3
    4
123454321
    4
    3
    2
    1
"""
      