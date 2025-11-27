principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter principle: "))
    if principle <= 0:
        print("Principle must be higher than 0.")

while rate <= 0:
    rate = float(input("Enter rate: "))
    if rate <= 0:
        print("Rate must be higher than 0.")

while time <= 0:
    time = int(input("Enter time: "))
    if time <= 0:
        print("Time must be higher than 0.")

final_amount = principle * pow(1 + rate/100, time)
print(f"Final amount: {final_amount:.3f}")

