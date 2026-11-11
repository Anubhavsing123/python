# Exercise 30. Remove duplicates without set
n=[1, 2, 2, 3, 4, 4, 4, 5]
m=[]
for i in n:
    if i not in m:
        m.append(i)
print(m)
