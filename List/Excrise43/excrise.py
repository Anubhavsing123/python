#Exercise 43. Move All Zeros to the End (Maintaining Order)
l=[0, 1, 0, 3, 12]
s=[]
m=[]
for i in l:
    if i!=0:
        s.append(i)
    else:
        m.append(i)
print(s+m)