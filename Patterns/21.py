n=int(input("enter n: "))
i=1
while i<=n:
   j=1
   while j<=i:
      if j==i or j==1 or i==n:
         print(i,end="")
      else:
         print(" ",end="")
      j=j+1
   print()
   i=i+1
"""
enter n: 5
1
22
3 3
4  4
55555
"""