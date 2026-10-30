#Exercise 14. Check if List Contains a Specific Item
d= ["Laptop", "Mouse", "Monitor", "Keyboard"]

for i in d:
    if "Laptop" in i:
        print(i)

inventory = ["Laptop", "Mouse", "Monitor", "Keyboard"]
target = "Tablet"

if target in inventory:
    print(f"Is {target} in inventory? True")
else:
    print(f"Is {target} in inventory? False")