#Rotate a List (Left or Right by k positions)
l=[1, 2, 3, 4, 5]
k=2
k=k%len(l)
s=[]
s=l[k:]+l[:k]
print(s)