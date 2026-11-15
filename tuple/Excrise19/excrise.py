#. Problem Statement: Write a Python program to find all elements that are common to two different tuples.
t1 = (1, 2, 3, 4, 5, 6) 
t2 = (4, 5, 6, 7, 8, 9)
l=tuple(x for x in t1 if x in set(t2))
print(l)


common = tuple(sorted(set(t1) & set(t2)))
print("Common elements:", common)