#Exercise 17. Write a Python program to modify a set so that it keeps only elements that are in either set but not in both, using the symmetric_difference_update() method.
a = {1, 2, 3, 4, 5} 
b = {3, 4, 5, 6, 7}
a.symmetric_difference_update(b)
print(a)