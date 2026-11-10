# Calculate Cumulative Sum (Prefix Sums)
l=[10,20,30,40]
s=0
m=[]
for i in l:
    s+=i
    m.append(s)
print(m)