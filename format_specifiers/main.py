# :<   → Left aligns the result (within the available space)
# :>   → Right aligns the result (within the available space)
# :^   → Center aligns the result (within the available space)
# :=   → Places the sign to the leftmost position
# :+   → Use a plus sign to indicate if the result is positive or negative
# :-   → Use a minus sign for negative values only
# :    → Inserts a space before positive numbers (and a minus sign before negative numbers)
# :,   → Use a comma as a thousand separator
# :_   → Use an underscore as a thousand separator
# :b   → Binary format
# :c   → Converts the value into the corresponding Unicode character
# :d   → Decimal format
# :e   → Scientific format, with a lowercase 'e'
# :E   → Scientific format, with an uppercase 'E'
# :f   → Fixed-point number format
# :F   → Fixed-point number format, uppercase (INF and NAN)
# :g   → General format
# :G   → General format (using uppercase 'E' for scientific notation)
# :o   → Octal format
# :x   → Hexadecimal format (lowercase)
# :X   → Hexadecimal format (uppercase)
# :n   → Number format (uses locale settings)
# :%   → Percentage format

price1 = 123456.78
price2 = -122.33
price3 = 452025
print(f"Price with :< = {price1:<10}")
print(f"Price with :> = {price2:>10}")
print(f"Price with :^ = {price3:^10}")

print(f"Price with := = {price3:=}")
