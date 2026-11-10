#Exercise 18.  Write a Python program to generate a dictionary of the squares of numbers from 1 to 10 using a dictionary comprehension in a single line.
d={k:k*k for k in range(1,11)}
print(d)