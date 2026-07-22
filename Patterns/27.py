n=int(input("enter n: "))
i=1
while i<=n:
   j=1
   while j<=i:
      if j==i or j==1 or i==n:
         if j%2!=0:
            print(1,end="")
         else:
            print(0,end="")
      else:
         print(" ",end="")
      j=j+1
   print()
   i=i+1
"""
enter n: 5
1
10
1 1
1  0
10101
"""

