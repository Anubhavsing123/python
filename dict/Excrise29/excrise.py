#Exercise 29.  Write a Python program to sort a dictionary’s items based on their values in ascending order.
scores = {"Alice": 88, "Bob": 72, "Charlie": 95, "Diana": 60}

s=dict(sorted(scores.items(),key=lambda i: i[1]))
print(s)