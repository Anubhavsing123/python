#Exercise 17.Write a Python program to update a value located multiple levels deep inside a nested dictionary structure.
data = {"school": {"department": {"class": {"teacher": "Mr. Smith", "students": 30}}}}
data["school"]["department"]["class"]["students"]=35
print(data)