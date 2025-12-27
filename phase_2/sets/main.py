s1 = {1, 2, 2, 3, 3, 3, 4}
print(f"s1: {s1}")

s2 = set([1, 2, 2, 5, 5, 4])
print(f"s2: {s2}")


# empty set
empty = set()

s2.add(22)
s2.remove(2)  # Error if not found
s2.discard(3423432)  # Safe remove

print(f"s2 after mod: {s2}")

s = {"John", "Alice"}
if "Alice" in s:
    print("Hi Alice!")

if not "Bob" in s:
    print("Bob ain't from here.")

# Set Math
print(f"Union: { s1 | s2}")
print(f"Intersection: { s1 & s2}")
print(f"Difference: { s1 - s2}")
print(f"Symmetric Difference {s1 ^ s2}")

# Compare
required = { "read", "write", "delete"}
user = {"read", "write", "delete", "copy"}

if required <= user:
    print("Access granted")

# Fast filtering

block = {"Scam", "Spam"}
words = {"Hello", "Spam", "Words"}
safe = {w for w in words if w not in block}
print(f"safe: {safe}")
