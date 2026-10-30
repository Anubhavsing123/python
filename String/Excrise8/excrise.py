#Find all occurrences of a substring in a given string by ignoring the case
#str1 = "Welcome to USA. usa awesome, isn't it?"
#Expected Output: The USA count is: 2
str1 = "Welcome to USA. usa awesome, isn't it?"
str2=str1.lower()
print(str2.count("usa"))
