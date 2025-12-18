user = {"name": "L", "age": 21, "role": "SWE"}

print(f"name = {user.get("name")}")

# Keys for dictionaries are
# Valid: str, int, float, tuple
# Invalid: list, dict, set
d = {("a", "b"): 1, 2: 2}
print(d[("a", "b")])

# Accessing Values
# When accessing values it's better to access with get key .get()
print(user.get("role"))
print(user.get("email", "Email not found!"))

# add and update
user["age"] = 22
user["email"] = "waiyanminlwin421@gmail.com"

print(user.get("email", "Email not found!"))

# delete
del d[2]
user.pop("role")
print(user)

# Looping dictionaries
for key in user:
    print(f"key: {key}")


for val in user.values():
    print(f"value: {val}")

for key, val in user.items():
    print(f"key: {key} , value: {val}")
