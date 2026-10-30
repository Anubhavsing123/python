# Write a Python program to check whether one set is a subset of another and whether one set is a superset of another using .issubset() and .issuperset().

set_a = {1, 2, 3} 
set_b = {1, 2, 3, 4, 5}
print(set_a.issubset(set_b))
print(set_a.issuperset(set_b))
print(set_b.issuperset(set_a))