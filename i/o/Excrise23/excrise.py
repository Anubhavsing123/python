# Exercise 23. Delete a specific file
import os

target = input("Enter filename to delete: ")

if os.path.exists(target):
    confirm = input(f"Are you sure you want to delete '{target}'? (y/n): ")
    if confirm.lower() == 'y':
        os.remove(target)
        print(f"File '{target}' has been deleted.")
    else:
        print("Operation cancelled.")
else:
    print("Error: File does not exist.")