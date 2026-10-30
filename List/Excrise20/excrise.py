#Exercise 20. Remove Duplicates from List
l=[10, 20, 10, 30, 40, 40, 20, 50]
s=set(l)
print(s)
d=list(dict.fromkeys(l))
print(d)
f=0
m={}
for i in l:
    if i in m:
        m[i]+=1
    else:
        m[i]=1
print(m)
for i,v in m.items():
    if v==1:
        print(i)
    else:
        pass





