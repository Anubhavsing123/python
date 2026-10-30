# Write a Python program to modify a set by removing all elements that are also found in another set using the difference_update() method.
a = {1, 2, 3, 4, 5} 
b = {3, 4, 5, 6, 7}
a.difference_update(b)
print(a)