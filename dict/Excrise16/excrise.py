# Write a Python program to change a specific value inside a dictionary that is nested within another dictionary.
company = {"name": "TechCorp", "location": {"city": "Berlin", "country": "Germany"}}
company["location"]["city"]="Munchi"
print(company)