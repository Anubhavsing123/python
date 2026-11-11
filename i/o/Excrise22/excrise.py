# Exercise 22. Check if file is empty
import os
file="txt.txt"
if os.path.exists(file):
    file_stat=os.stat(file)
    if file_stat.st_size==0:
        print(f"Status: {file} is empty.")
    else:
        print(f"Status: {file} size is {file_stat.st_size} bytes.")
else:
    print("File not found.")