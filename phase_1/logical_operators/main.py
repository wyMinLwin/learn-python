# Logical Operators
# or and not

user = "L"
is_active = False

if user and is_active:
    print(f"{user} is active")
elif user and not is_active:
    print(f"{user} is not active")
