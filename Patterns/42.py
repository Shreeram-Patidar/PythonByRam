n=int(input("enter n: "))
i=1
while i<=n:
      j=n
      while j>=i:
            print(j,end="")
            j=j-1
      print()
      i+=1
"""
enter n: 5
54321
5432
543
54
5
"""