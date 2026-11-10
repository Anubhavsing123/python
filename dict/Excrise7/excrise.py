# Write a Python program to access the value associated with the key 'history' from a dictionary nested within a larger data structure.
student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}

print(student["grades"]['history'])