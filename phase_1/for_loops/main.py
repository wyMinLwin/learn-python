# for loops

for x in reversed(range(-3,11,2)):
    if x == 3:
        continue
    elif x == 1:
        print("Honored one")
        break
    else:
        print(x)

text = "Nah I'd win"
for x in text:
    print(x)

