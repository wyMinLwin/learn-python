text = input("Enter a text: ")
text_count = len(text)

result = ""

for i in reversed(range(0,text_count)):
    result += text[i]

print(result)
