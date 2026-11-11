# Exercise 27. List Cumulative Sum: Each element is the sum of all previous
n= [1, 2, 3, 4]
s=0
m=[]
for i in n:
    s=s+i
    m.append(s)
print(m)

