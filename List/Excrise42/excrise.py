#Exercise 42. Split List into Chunks of Size N
l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n=3

def chuck(l,n):
    return [l[i:i+n]  for i in range(0,len(l),n)]
c=chuck(l,n)
print(c)
