#Write a Python program to create a new set containing only the elements from an existing set that satisfy a condition – specifically, elements divisible by 3.

numbers = {1, 2, 3, 6, 7, 9, 12, 14, 15}
d3=set()
for i in numbers:
    if i%3==0:
        d3.add(i)
print(d3)