temperature  = float(input("Enter temperature?: "))
unit = input("Celsius or Fahrenheit (C,F)?: ")

if unit == "C":
    result = round((temperature * 9/5) + 32, 2)
    print(f"It is {result}°F")
elif unit == "F":
    result = round((temperature - 32) * 5/9, 2)
    print(f"It is {result}°C")
else:
    print(f"{unit} is not valid!")
