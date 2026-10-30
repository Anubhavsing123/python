#Practice Problem: Write a program to count the total number of vowels (a, e, i, o, u) in a given string.

#Given Input: str1 = "Hello World"

#Expected Output: Vowel Count: 3

def vowel(str1):
    v="aieou"
    c=0
    for char in str1:
        if char in v:
            c+=1
#     return c
# c=vowel("Hello World")
print(c)


text = input("Enter a string: ")

vowels = sum(1 for ch in text.lower() if ch in "aeiou")

print("Total vowels:", vowels)
