# Weight Converter

weight = float(input("Enter your weight: "))
unit = input("Kilogram or Pound? (K,L): ")


if unit == "K":
    result = round(weight * 2.205, 2)
    print(f"You weight is {result} Lbs.")
elif unit == "L":
    result = round(weight / 2.205, 2)
    print(f"You weight is {result} Kgs.")
else:
    print(f"{unit} is not valid!")
