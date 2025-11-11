import time

input_time = int(input("Enter time in seconds: "))

for t in range(input_time, 0, -1):
    seconds = t %  60
    minutes = int(t / 60) % 60
    hours = int(t/ 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Oop! Time's up!")
