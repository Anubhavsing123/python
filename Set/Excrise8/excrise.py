#Write a Python program to find all elements that are in either Set A or Set B, but not in both.
set_a = {1, 2, 3, 4} 
set_b = {3, 4, 5, 6}
print(set_a.symmetric_difference(set_b))
print(set_b.symmetric_difference(set_a))