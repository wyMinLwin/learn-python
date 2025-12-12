# A list is an ordered, changeable collection of items.
numbers = [1, 2, 3, 4, 5000]
names = ["Bruce", "L"]
mixed = ["Bruce", 1, True, 3.14]

# Indexing
print(f"first item: {mixed[0]}")
print(f"last item: {mixed[-1]}")

# Slicing
print(mixed[1:3])
print(mixed[:3])
print(mixed[2:])
print(mixed[:])
print(mixed[::-1])

# Mutability
mixed[0] = "Batman"
print(mixed)

# Common List Methods

# append -> (add to end)
numbers.append(66)

# insert -> (add to position)
numbers.insert(0, 0)

# remove -> remove first match
numbers.remove(5000)

# pop -> remove by index
numbers.pop(2)

# clear -> clear all
mixed.clear()

# extend -> merge lists
names.extend(["Itachi", "Gojo"])

print(numbers)
print(names)
print(mixed)

# Looping a list
for name in enumerate(names):
    print(name)

if "Wai" in names:
    print("Hi Wai!")
else:
    print("Where is Wai?")

mod_names = ["Mr. " + name for name in names if len(name) > 1]
print(f"mod names: {mod_names}")

# Nested arrays
nested_array = [
    [1,2,3],
    [4,5,6]
]
print(nested_array[1][0])
