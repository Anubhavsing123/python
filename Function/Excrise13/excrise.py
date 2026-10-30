# Write a recursive function to calculate the factorial of a non-negative integer.
def fac(num):
    if num==0:
        return 1
    else:
        return num*fac(num-1)
c=fac(5)
print(c)