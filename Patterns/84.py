n=int(input("enter n: "))
i=1
while i<=n:
      s=1
      while s<=n-i:
            print(" ",end="")
            s=s+1
      j=i
      while j>=1:
            print(j,end="")
            j=j-1
      k=2
      while k<=i:
            print(k,end="")
            k=k+1
      print()
      i=i+1
"""
enter n: 5
    1
   212
  32123
 4321234
543212345
"""