amount=int(input("Amount ="))
note100=amount//100
amount=amount%100
note50=amount//50
amount=amount%50
note10=amount//10
amount=amount%10
print("$100*",note100)
print("$50*",note50)
print("$10*",note10)