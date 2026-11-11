# Exercise 18. Read a file and store its content in a list
with open("test.txt", "r") as f:
    lines = f.readlines()
    print(lines)
 