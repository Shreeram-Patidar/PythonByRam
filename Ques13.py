principal=int(input("Principle ="))
rate=int(input("Rate ="))
time=int(input("Time ="))
amount=principal*((1+(rate/100))**time)
ci=amount-principal
print("Amount =",amount)
print("Compound Intrest =",ci)