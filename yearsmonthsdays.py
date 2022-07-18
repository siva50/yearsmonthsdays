days = int(input("enter total days"))
years = days//365
days = days%365
month = days//31
days = days%31
days = days%7
print(years,"Years",month,"Month",days,"Days")

