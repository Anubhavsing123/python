#Exercise 28. Extract Every Nth Element from a List
l=['a', 'b', 'c', 'd', 'e', 'f', 'g']
n=3
l=[l[i] for i in range(0,len(l),n)]
print(l)

