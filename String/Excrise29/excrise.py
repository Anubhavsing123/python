
def is_unique(s):
    # A set only keeps unique elements
    char_set = set(s)
    return len(char_set) == len(s)

str1 = "python"
str2 = "alphabet"

print(f"'{str1}' unique: {is_unique(str1)}")
print(f"'{str2}' unique: {is_unique(str2)}")