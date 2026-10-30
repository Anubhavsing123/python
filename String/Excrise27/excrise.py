#Write a program to check if a string is a palindrome (reads the same forward and backward).
str1="madam"
str2=str1[::-1]
print(str2)
if str2==str1:
    print("True")
else:
    print("False")
    