#32 Write a Python program to sort a dictionary’s items by the length of their string values, from shortest to longest.
words = {"a": "banana", "b": "kiwi", "c": "strawberry", "d": "fig"}

s=dict(sorted(words.items(),key=lambda x: len(x[1])))
print(s)