n=int(input("enter n: "))
i=n
while i>=1:
      j=1
      while j<=i:
            if i==n or j==1 or i==j: 
               print(i,end="")
            else:
               print(" ",end="")
            j=j+1
      print()
      i=i-1
"""
enter n: 5
55555
4  4
3 3
22
1
"""