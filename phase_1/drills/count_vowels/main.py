text = input("Enter text: ")
text_count = len(text)

result = 0
for i in range(0, text_count): 
    char = text[i]
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        result += 1

if result == 1: 
    print(f"There is {result} vowel in your sentence")
elif result > 1:
    print(f"There are {result} vowels in your sentence")
else: 
    print(f"There is {result} vowel in your sentence")
