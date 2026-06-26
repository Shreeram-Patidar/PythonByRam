"""
Count Factors of Number
A mathematics learning app gives practice questions where students must know how many factors a number has. The app should automatically count the total factors of the entered number.
Write a program to count total factors of a number using loops.

Input:
12

Output:
Factors Count = 6
"""
num=int(input("Entert number"))
i=0
count=0
while i<=n//2:
      if(num%i==0):
          count+=1
      i+=1
print(count)
