name = input("Enter your name_ ")

while name == "":
    print("You didn't enter your name!")
    name = input("Enter your name_ ")

print(f"Hello {name}!")

food = input("Enter food (:q to quit)_ ")

while not food == ":q":
    print(f"{name} ordered {food}")
    food = input("Enter food again (:q to quit)_ ")

print(f"Bye {name}~~~~")

