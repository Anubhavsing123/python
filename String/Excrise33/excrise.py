#: Given two strings of equal length, merge them by alternating characters.
s1 = "ABC"
s2 = "xyz"
r=len(s1)
res=[]
for i in range(r):
    res.append(s1[i]+s2[i])
    
print("".join(res))