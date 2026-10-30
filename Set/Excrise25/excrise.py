# Write a Python program to create a frozenset, demonstrate that set operations work on it, and confirm that any attempt to modify it raises a TypeError.

fs=frozenset([1,2,3,4])
print(fs)
print(fs.intersection({5,6,7}))
print(fs)
try:
    fs.add(6)
except AttributeError as e:
    print(e)