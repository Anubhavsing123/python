#Exercise 24.: Write a Python program to find all keys that exist in the first dictionary but are absent from the second dictionary.
d1 = {"a": 1, "b": 2, "c": 3} 
d2 = {"b": 20, "d": 40}
f=d1.keys() - d2.keys()
print(f)