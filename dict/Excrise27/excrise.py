#Exercise 27. Write a Python program to remove all key-value pairs from a dictionary where the value is None
data = {"name": "Alice", "age": None, "city": "Paris", "score": None}
s= {k : data[k] for k in data if data[k] is not None}
print(s)