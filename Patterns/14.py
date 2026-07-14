n=int(input("enter n: "))
i=1
count=1
while i<=n:
   j=1
   while j<=i:
      print(count,end="")
      count+=1
      j+=1
   print()
   i+=1
"""
enter n: 4
1
23
456
78910
"""