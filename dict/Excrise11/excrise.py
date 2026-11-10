#  Write a Python program to verify whether a specific value is present anywhere in a dictionary.
roles = {"alice": "admin", "bob": "editor", "carol": "viewer"}
print("editor" in roles.values())
print("hello" in roles.values())