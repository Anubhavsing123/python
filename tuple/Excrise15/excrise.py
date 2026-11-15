# Problem Statement: Write a Python program to sort a tuple of tuples based on the second item in each nested tuple.

students = (("Alice", 88), ("Bob", 73), ("Charlie", 95), ("Diana", 61))


l=sorted(students,key=lambda x:x[1])
print(l)