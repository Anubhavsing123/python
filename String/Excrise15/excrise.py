#Practice Problem: Use the .partition() method to split a string into three parts: 
# the part before a separator, the separator itself, and the part after it.
str1 ,sep= "username@company.com", "@"
print(id(str1))
str1=str1.partition("@")

print(id(str1))
print(str1)