#Exercise 35. Remove Negative Numbers In-place
l=[10, -5, 20, -1, 0, -8]
for i in range(len(l)-1,-1,-1):
    if l[i]<0:
        del l[i]
print(l)
