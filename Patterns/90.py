n=int(input("enter n: "))
i=1
while i<=n:
      j=1
      while j<=n:
            if i==j or j+i==n+1:
               print("*",end="")
            else:
               print(" ",end="")
            j=j+1
      print()
      i=i+1
"""
enter n: 10
*        *
 *      *
  *    *
   *  *
    **
    **
   *  *
  *    *
 *      *
*        *
"""