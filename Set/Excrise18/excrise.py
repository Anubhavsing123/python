# Write a Python program to remove a batch of specific items from a set all at once using the difference_update() method.
items = {10, 20, 30, 40, 50, 60} 
to_remove = {20, 40, 60}
items.difference_update(to_remove)
print(items)

