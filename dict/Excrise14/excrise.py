# Write a Python program that uses zip() to combine a list of keys and a list of values into a single dictionary.
attributes = ["brand", "model", "year", "color"] 
details = ["Honda", "Civic", 2023, "silver"]
s=dict(zip(attributes,details))
print(s)
