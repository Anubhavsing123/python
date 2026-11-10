#  : Write a Python program to remove a specific key from a dictionary, 
# retrieve all key-value pairs, and check whether a given key exists.
car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}

car.pop("year")
print(car)
print(car.items())
print("brand" in car)
print("year" in car)