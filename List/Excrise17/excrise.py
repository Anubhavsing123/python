#Exercise 17. Count Occurrences of an Item
l=[10, 20, 30, 10, 40, 10, 50]
target=10
s=l.count(10)
print(s)
c=0
for i in l:
    if i==target:
        c=c+1
print(c)
