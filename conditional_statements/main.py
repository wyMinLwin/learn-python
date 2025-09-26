age = int(input("Enter you age: "))
print(age)

if age >= 1 and age <= 25:
    print("You are Young Prodigy 🌱")
elif age >= 26 and age <= 40:
    print("You are Rising Explorer 🔥")
elif age >= 41 and age <= 60:
    print("You are Seasoned Challenger ⚔️")
elif age >= 61:
    print("You are Wise Elder 🕊️")
else:
    print("Please add proper age")




is_online = True

if is_online:

    print("Connected")
    
    user = input("who are you?: ")
    if user == "L":
        print("Welcome L 💻")
    else:
        print("LIAR!")
else: 
    print("Disconnected")
