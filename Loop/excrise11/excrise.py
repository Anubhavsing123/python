#  Reverse a string using a for loop (no slicing).
s="Python"
for i in range(len(s)-1,-1,-1):
    print(s[i],end="")

#m2
original_str = "Python"
reversed_str = ""

for char in original_str:
    # Prepending: Put the new character before the existing ones
    reversed_str = char + reversed_str

print(f"Original: {original_str}")
print(f"Reversed: {reversed_str}")