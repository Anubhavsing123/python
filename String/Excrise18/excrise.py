#Count all letters, digits, and special symbols from a given string
str1 = "P@#yn26at^&i5ve"
l,d,s=0,0,0
for ch in str1:
    
    match ch:
        case ch if ch.isalpha():
            l+=1
        case  ch if ch.isdigit():
            d+=1
        case _:
            s+=1
print(l,s,d,end=" \n")
def count_chars_digits_symbols(sample_str):
    char_count = 0
    digit_count = 0
    symbol_count = 0
    for char in sample_str:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        # if it is not letter or digit then it is a special symbol
        else:
            symbol_count += 1

    print("Chars =", char_count, "Digits =", digit_count, "Symbol =", symbol_count)

sample_str = "P@#yn26at^&i5ve"
print("total counts of chars, digits, and symbols")
count_chars_digits_symbols(sample_str)