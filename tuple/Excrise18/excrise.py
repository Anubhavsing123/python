# Problem Statement: Write a Python program to zip two tuples together – one holding keys and the other holding values – to create a dictionary.



keys = ("name", "age", "city") 
values = ("Alice", 30, "Pune")
l=dict(zip(keys,values))
print(l)
