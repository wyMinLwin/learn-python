# Input

item = input("What item do you want to buy?: ")
price = float(input(f"How much {item} is?: "))
quantity = int(input(f"How many of {item} do you want?: "))

print(f"You have purchased {item} x {quantity}")
print(f"TOTAL PRICE: {price * quantity}")
