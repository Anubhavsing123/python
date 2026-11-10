#Exercise 34. Write a Python program to convert a nested dictionary into a formatted JSON string with readable indentation.
import json
person = {"name": "Alice", "age": 30, "address": {"city": "Mumbai", "pin": "400001"}}
print(json.dumps(person,indent=4))