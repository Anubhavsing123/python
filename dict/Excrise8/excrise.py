#Write a Python program to create a dictionary from a list of keys, assigning the same default value to every key.
keys = ["math", "science", "english", "history"] 
default = 0

score=dict.fromkeys(keys,default)
print(score)
l={k: default for k in keys}
print(l)