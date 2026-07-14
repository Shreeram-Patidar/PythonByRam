n=int(input("enter n: "))
i=1
while i<=n:
   j=1
   while j<=i:
      if i%2==0:
         print("#",end="")
      else:
         print("*",end="")
      j=j+1
   print()
   i=i+1
"""
*
##
***
####
*****
"""
    