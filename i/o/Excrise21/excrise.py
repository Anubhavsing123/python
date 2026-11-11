# Exercise 21. Read line number 4 from a file

# Opening the file in read mode
with open("txt.txt", "r") as f:
    # Read all lines into a list
    lines = f.readlines()
    # Print the 4th line (index 3)
    print(lines[3])