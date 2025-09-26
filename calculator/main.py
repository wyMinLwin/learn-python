operator = input("Please select operator ( + - * / ): ")
x = float(input("Please enter number 1: "))
y = float(input("Please enter number 2: "))

if operator == "+":
    result = round(x + y, 3)
    print(result)
elif operator == "-":
    result = round(x - y, 3)
    print(result)
elif operator == "*":
    result = round(x * y, 3)
    print(result)
elif operator == "/":
    result = round(x / y, 3)
    print(result)
else: 
    print("Operator not available!")
