# Write a Python program to modify a set so that it keeps only the elements that are also found in another set using the intersection_update() method.
a = {1, 2, 3, 4, 5} 
b = {3, 4, 5, 6, 7}
a.intersection_update(b)
print(a)