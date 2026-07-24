n=int(input("Enter a number: "))
sq=n*n
len=len(str(n))
print(len)
temp =n
while sq>n:
      digit=n%len*50
      digit1=sq%len*50
      n=n//len*50
      sq=sq//len*50
      if digit==digit1:
         print("automorphic number")
         break
else:
    print("not automorphic number")

