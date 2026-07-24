n=int(input("enter n: "))
i=1
while i<=n:
      s=1
      while s<=n-i:
            print(" ",end="")
            s=s+1
      j=1
      while j<=i:
            if j%2!=0:  
               print(1,end="")
            else:
               print(0,end="")
            j=j+1
      print()
      i=i+1
"""
enter n: 5
    1
   10
  101
 1010
10101
"""