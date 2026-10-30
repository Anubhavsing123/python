#Exercise 27. Find the Most Frequent Element
l=[1, 3, 3, 2, 1, 1, 4, 3, 3]
m={}
for i,k in enumerate(l):
    if k in m:
        m[k]+=1
    else:
        m[k]=1
print(max(m,key=m.get))


