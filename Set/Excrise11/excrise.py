#Write a Python program to add multiple elements from a list into an existing set using the .update() method.
fruits = {"apple", "banana"} 
new_fruits = ["cherry", "mango", "apple"]
fruits.update(new_fruits)
print(fruits)
fruits = {"apple", "banana"}
new_fruits = ["cherry", "mango", "apple"]

fruits.update(new_fruits)
print("Updated set:", fruits)
