#Write a Python program to create a dictionary by mapping two equal-length lists, one containing keys and the other containing values.

keys = ["name", "age", "city"] 
values = ["Bob", 25, "London"]
d=dict(zip(keys,values))
print(d)
c={k:v for k,v in zip(keys,values)}
print(c)