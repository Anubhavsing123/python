# Write a Python program to remove duplicate values from a list while preserving the original order of first appearances.
items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

s=set()
r=[]
for i in items:
    if i not in s:
        r.append(i)
        s.add(i)


print(r)