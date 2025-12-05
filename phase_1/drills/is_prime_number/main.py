n = int(input("Enter a number: "))

if n <= 1:
    print(f"{n} is not a prime number.")
    exit()
elif n == 2:
    print(f"{n} is prime number.")
    exit()

# n - 1 = 2^s * d
n_minus_one = n - 1
# find s and d
s = 0
d = 0
dividend = n_minus_one
if dividend % 2 != 0:
    d = dividend
else:
    while dividend % 2 == 0:
        dividend //= 2
        s += 1
        d = dividend

# let base a = 2
a = 2

x = 0
# x = a^d mod n
x = pow(a, d, n)

if s == 0:
    if x == 1 or x == n - 1:
        print(f"{n} is prime number.")
    else:
        print(f"{n} is not prime number.")
    exit()

for i in range(s):
    # x = x^2 mod n
    x = pow(x, 2, n)
    if x == 1 or x == n - 1:
        print(f"{n} is prime number.")
        exit()
    elif i == s - 1:
        print(f"{n} is not prime number.")
