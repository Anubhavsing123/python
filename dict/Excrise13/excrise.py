#  Write a Python program to create a new dictionary containing only a specified subset of keys from an existing dictionary.
user = {"id": 42, "username": "jdoe", "email": "jdoe@example.com", "password": "s3cr3t", "joined": "2021-03-15"} 
k = ["id", "username", "email"]
l={ k: user[k] for k in k}
print(l)