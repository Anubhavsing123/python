# Exercise 18. Collatz Conjecture: Generate a sequence until it reaches 1
n=6
print(n,end=" ")
while n>1:
    if n%2==0:
        n=n//2
    else:
        n=(n*3)+1
    print(f'{n}' ,end=" ")