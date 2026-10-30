#   Write a Python program to demonstrate that a set can store tuples as elements but cannot store lists, and explain why this difference exists.
s= {(1, 2), (3, 4), (5, 6)}
print(s)
try:
    bad_set = {[1, 2], [3, 4]}
except TypeError as e:
    print("Error:", e)
 