#Write a Python program to check whether all values in a dictionary are distinct (i.e., no two keys share the same value).

data = {"a": 1, "b": 2, "c": 3, "d": 2}

values = list(data.values())
is_unique = len(values) == len(set(values))

print(is_unique)