menu : list[str] = [ ]
#Pizza , Spaghetti , Fish

menu.insert(0,"pizza")
menu.insert(1,"spaghetti")
menu.insert(2,"fish")
print(menu)

menu.remove("spaghetti")
print(menu)

if "spaghetti" in menu:
    print(True)

else:
    print(False)

prices: list[float]=[4.0 , 6.5]
print(prices)

max_number = max(prices)
print("The largest number is:",max_number)

min_number = min(prices)
print("The lower number is:",min_number)

prices.remove(max_number)
print(prices)

