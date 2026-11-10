#Exercise 36. Write a Python program to invert a dictionary where multiple keys may share the same value. Instead of overwriting, group all original keys that map to the same value into a list under that value as the new key.

original = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
d={}
for k,v in original.items():
    d.setdefault(v,[]).append(k)
print(d)