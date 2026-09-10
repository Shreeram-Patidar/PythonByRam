n=int(input("enter n: "))
i=1
while i<=n:
      s=1
      while s<=n-i:
            print(" ",end="")
            s=s+1
      j=1
      while j<=i*2-1:
            if j%2!=0:
               print("*",end="")
            else:
               print("_",end="")
            j=j+1
      print()
      i=i+1
n1=n-1
x=n1
while x>=1:
      s=0
      while s<=n1-x:
            print(" ",end="")
            s=s+1
      y=1
      while y<=x*2-1:
            if y%2!=0:
               print("*",end="")
            else:
               print("_",end="")
            y=y+1
      print()
      x=x-1
"""
enter n: 5
    *
   *_*
  *_*_*
 *_*_*_*
*_*_*_*_*
 *_*_*_*
  *_*_*
   *_*
    *
"""
            