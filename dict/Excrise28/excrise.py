#Exercise 28. Write a Python program to sort a dictionary by its keys and return the result as a new dictionary with items in ascending key order.

data = {"banana": 3, "apple": 5, "cherry": 1, "date": 4}
s=dict(sorted(data.items()))
print(s)