#Exercise 31. Filter Strings by Length in a List
l=["apple", "pie", "banana", "kiwi", "pear"]
k=5
l=[i for i in l if len(i)>=k]
print(l)