n=int(input("enter n: "))
i=n
while i>=1:
      s=1
      ch=65
      while s<=n-i:
            print(" ",end="")
            s=s+1
      j=1
      while j<=i:
            if i==n or j==1 or j==i:
               print(chr(ch),end="")
            else:
               print("_",end="")
            j=j+1
            ch=ch+1
      print()
      i=i-1
"""
enter n: 5
ABCDE
 A__D
  A_C
   AB
    A
"""