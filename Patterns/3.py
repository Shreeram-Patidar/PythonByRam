n=int(input("enter n: "))
i=1
while i<=n:
    space=0
    while space<i:
        print(" ",end="")
        space+=1
    print("*")
    i=i+1
"""
enter n: 5
 *
  *
   *
    *
     *
"""