# Problem Statement: Write a Python program to apply a square function to every item in a tuple using map(), and also demonstrate the equivalent generator expression approach.

numbers = (1, 2, 3, 4, 5, 6)
t=map(lambda x: x**2,numbers)
print(t)
print(tuple(t))