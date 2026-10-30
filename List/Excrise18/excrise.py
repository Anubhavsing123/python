#Exercise 18. Remove All Occurrences of a Specific Item
l=[5, 20, 15, 20, 25, 50, 20]
target=20
c=[x for x in l if x!=target]
print(c)