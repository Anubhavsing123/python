#Exercise 9.  Write a Python program to rename an existing key in a dictionary while preserving its associated value and the rest of the dictionary unchanged.
employee = {"fname": "John", "age": 30, "dept": "Engineering"}
employee["first_name"]=employee.pop('fname')
print(employee)
