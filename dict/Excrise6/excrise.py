#  Write a Python program to retrieve a specific value from a dictionary that is nested inside another dictionary
person = {"name": "Carol", "address": {"city": "Paris", "zip": "75001"}}
print(person["address"]["city"])
print(person["address"]["zip"])