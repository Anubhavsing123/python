#Exercise 45.  Find All Subsets of a List (Power Set)
l=[1,2,3]
d=len(l)
m=[[]]
for i in l:
        for k in m:
                m.append(k,i)
                
print(m)
