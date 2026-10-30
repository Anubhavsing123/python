# Write a Python program to calculate the total sum of all elements in a set manually using a loop, without using the built-in sum() function.
numbers = {10, 20, 30, 40, 50}
s=0
for i in numbers:
    s+=i
print(s)