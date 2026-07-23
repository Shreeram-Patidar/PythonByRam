n=int(input("enter n: "))
i=n
while i>=1:
      j=1
      x=i
      y=1
      while j<=i:
            if i%2!=0:
               print(x,end="")
               x=x-1
            else:
               print(y,end="")
               y=y+1
            j=j+1    
      print()
      i=i-1
"""123456
54321
1234
321
12
1
"""
            