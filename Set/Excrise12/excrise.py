#Write a Python program to add elements from a list, a tuple, and another set into an existing set in a single .update() call.

base = {1, 2}
from_list = [3, 4]
from_tuple = (5, 6)
from_set = {7, 8}
s=set()
s.update(base,from_list,from_set,from_tuple)
print(s)