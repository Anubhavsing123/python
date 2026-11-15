# Problem Statement: Write a Python program to access a specific element that is stored inside a tuple which is itself nested inside another tuple.
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
row=matrix[1][2]
print(row)