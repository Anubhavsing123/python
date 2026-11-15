# Problem Statement: Write a Python program to filter a tuple and keep only the elements that satisfy a given condition, using both filter() and a list comprehension approach.

numbers = (3, 14, 7, 22, 9, 41, 18, 5)
x=tuple(filter(lambda x:x>10,numbers))
print(x)
filtered_comp = tuple(x for x in numbers if x > 10)
print("Using comprehension:", filtered_comp)
 