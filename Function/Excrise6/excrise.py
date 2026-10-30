# Write a recursive function addition() that calculates the sum of numbers from 0 to 10. A recursive function is a function that calls itself to solve smaller instances of the same problem.
def add(num):
    if num:
        return num + add(num-1)
    else:
        return 0
c=add(10)
print(c)