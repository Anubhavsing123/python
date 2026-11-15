# Create a tuple that contains a list as one of its elements. Modify the list in place and observe that the tuple’s identity stays the same while its contents appear to change.

t = (91, 2, [3, 4, 5])
print(t)
print(id(t))

t[2].append(99)

print("After: ", t)
print("Tuple id after: ", id(t))
print("Same object?", id(t) == id(t))