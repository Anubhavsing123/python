#Exercise 38. Flatten Nested List (2D to 1D)
i= [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
s=[]
for l in i:
    s.extend(l)
print(s)