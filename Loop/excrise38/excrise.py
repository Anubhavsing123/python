# Exercise 38. Find the sum of the series up to n terms
s=2
u=0
for i in range(0,6):
   #print(s,end=" +")
   u+=s
   s=s*10+2
print(u,)
   