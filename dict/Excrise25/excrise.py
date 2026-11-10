#Exercise 25.  Write a Python program to create a new dictionary containing only the key-value pairs that are identical in both input dictionaries.
d1 = {"a": 1, "b": 2, "c": 3} 
d2 = {"a": 1, "b": 99, "c": 3}
s={ k:d1[k]  for k in d1.keys() & d2.keys() if d1[k]==d2[k]}
print(s)