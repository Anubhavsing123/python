#  Write a Python program to combine two dictionaries into a single dictionary. If both dictionaries share a key, the value from the second dictionary should take precedence.

dict1 = {"a": 1, "b": 2} 
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)
print(dict1)
m={**dict1,**dict2}
print(m)
merged = dict1 | dict2
print(merged)