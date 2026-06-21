total=int(input("Enter the event duration: "))
hour=total//3600
total=total%3600
minut=total//60
total=total%60
second=total
print(hour,":hour",minut,":minute",second,":second")