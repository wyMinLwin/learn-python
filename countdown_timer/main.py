import time

input_time = int(input("Enter time in seconds: "))

for t in range(input_time, 0, -1):
    print(t)
    time.sleep(1)

print("Oop! Time's up!")
