# Exercise 29. Find common elements (Intersection) using loop
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common=[]
for i in list_a:
    if i in list_b:
        common.append(i)
print(common)
        