n=int(input("enter n: "))
i=1
while i<=n:
      s=1
      while s<=n-i:
            print(" ",end="")
            s=s+1
      j=1
      while j<=i*2-1:
            if j==1 or i==n or j==i*2-1:
               print(1,end="")
            else:
               print("*",end="")
            j=j+1
      print()
      i=i+1
"""
enter n: 5
    1
   1*1
  1***1
 1*****1
111111111
"""