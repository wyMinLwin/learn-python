text = input("say something: ")

print(f"len() = {len(text)}")
print(f"find() = {text.find("s")}")
print(f"rfind() = {text.rfind("s")}")

print(f"capitalize() = {text.capitalize()}")
print(f"upper() = {text.upper()}")
print(f"lower() = {text.lower()}")

print(f"{text}.isdigit() = {text.isdigit()}")
print(f"{text}.isalpha() = {text.isalpha()}")

print(f"{text}.count(\"-\") = {text.count("-")}")
print(f"{text}.replace( \"-\" , \"#\") = {text.replace("-","#")}")
