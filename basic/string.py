
escape = "    \"Learning python\""

print(escape)
print("Upper: " + escape.upper())
print("Lower: " + escape.lower())
print("Title: " + escape.title())
print("Strip: " + escape.strip()) # rstrip -> Right Side Strip, lstrip -> Left Side Strip
print(escape.find("py"))
print(escape.find("yp"))
print("Replace" + escape.replace("Learning", "Mastering"))
print("py" in escape)
print("Jerome" not in escape)
