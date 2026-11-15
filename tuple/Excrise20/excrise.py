# Problem Statement: Write a Python program to “modify” a tuple by converting it to a list, changing a specific item, and converting it back to a tuple.
colours = ("red", "green", "blue")

l=list(colours)
l[1]="yellow"
print(l)
print(colours)