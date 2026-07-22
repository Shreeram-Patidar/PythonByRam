n=int(input("enter n: "))
i=n
while i>=1:
   j=n
   while j>=i:
      print(j,end="")
      j=j-1
   print()
   i=i-1
"""
enter n: 5
5
54
543
5432
54321
"""