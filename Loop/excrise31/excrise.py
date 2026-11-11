# Exercise 31. Even/Odd Segregation: Move evens to front, odds to back
n=[1, 2, 3, 4, 5, 6]
#m1


even = [i for i in n if i % 2 == 0]
odd = [i for i in n if i % 2 != 0]

result = even + odd

print(result)
#m2
left=0
right=len(n)-1
while left<right:
    if n[left]%2==0:
        left+=1
    elif n[right]%2!=0:
        right-=1
    else:
        n[left],n[right]=n[right],n[left]
        left+=1
        right-=1
print(n)
