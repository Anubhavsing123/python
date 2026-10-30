#Write a program to extract only the numeric digits from a mixed string and combine them into a single string.
str1 = "I am 25 years and 10 months old"
res=""
for ch in str1:
    if ch.isdigit():
        res+=ch
print(res)
str1 = "I am 25 years and 10 months old"
print("Original string is:", str1)

# Joining only the digits found in the string
res = "".join([item for item in str1 if item.isdigit()])

print("Resulting digits:", res)