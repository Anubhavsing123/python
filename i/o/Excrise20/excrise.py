# Exercise 20. Count total lines in a file
c=0
with open("txt.txt","r") as f:
    for l in f:
        c+=1
print(f"The file contains {c} lines.")