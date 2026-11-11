# Exercise 39. flatten a nested list using loops
nested_list = [[10, 20], [30, 40], [50, 60]]
m=[]
# for i in nested_list:
#     m.extend(i)
# print(m)
for i in nested_list:
    for j in i:
        m.append(j)
print(m)