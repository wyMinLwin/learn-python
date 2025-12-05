number = int(input("Enter input nubmer: "))

for i in range(1, number + 1):
    print(i)
    if i % 2 == 0:
        print(f"{i} is even number.")
