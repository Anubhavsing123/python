# Exercise 13. Count total number of digits in a number
n=75869
c=0
#m-1
# while n>0:
#     n=n//10
#     c+=1
# print(c)
while n>0:
    digit=n%10
    c+=1
    n//=10
print(c)