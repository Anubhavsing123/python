# Exercise 34. Display fibonacci series up to 10 terms
n=0
n1=1
s=0
for i in range(10):
    print(n,end=" ")
    s=n+n1
    n=n1
    n1=s
