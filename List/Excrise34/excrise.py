#Exercise 34. Find the Difference Between Two Lists
a=[1, 2, 3, 4, 5]
b= [2, 4, 6]
s=set(b)
print(s)
l=[i for i in a if i in s ]
print(l)