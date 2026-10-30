#Exercise 26. Find the Second Largest Number in a List
l=[12, 35, 1, 10, 34, 1, 35]
s=set(l)
print(s)
max1=max(s)
s.remove(max1)
max2=max(s)
print(max2)

l = [12, 35, 1, 10, 34, 1, 35]

largest = float("-inf")
second = float("-inf")
print(second)

for i in l:
    if i > largest:
        second = largest
        largest = i

    elif i > second and i != largest:
        second = i

print("Largest:", largest)
print("Second Largest:", second)