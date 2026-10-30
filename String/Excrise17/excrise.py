#Write a program to arrange string characters such that all lowercase letters come first, followed by all uppercase letters.
str1 = "PyNaTive"
def change(str1):
    l=""
    u=""
    for char in str1:
        if char.islower():
            l+=char
        else:
            u+=char
    return l+u
            
    
c=change(str1)
print(c)
str1 = "PyNaTive"
lower = []
upper = []

for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)

# Join both lists
res = "".join(lower + upper)
print("Result:", res)

