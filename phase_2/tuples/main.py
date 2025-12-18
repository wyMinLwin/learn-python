RGB_RED = (255, 0, 0)
# can create like this too RGB_RED = 255,0,0
print(RGB_RED)


# If single item tuple it's importand to create like this
single = (1,)
# If you do like this (1), I would be an int

# accessing tuples
lang = ("Python", "JavaScript", "Rust")
print(lang[1])
print(lang[-1])

print(lang[0:2])

# types are immutable
# so if we do this lang[2]= "C#" , it's basically a type error

# we can mutate the content
t = (["C", "Rust"], ["JavaScript", "Python"])
print(f"Original t: {t}")

t[0].append("Go")

# Unpack Tuple
points = (10, 20)
x, y = points
print(f"x,y = {x},{y}")
print("swap x and y")
x, y = y, x
print(f"x,y = {x},{y}")

# Entended Unpacking
*il, cl = lang
print(f"il: {il}, cl: {cl}")
