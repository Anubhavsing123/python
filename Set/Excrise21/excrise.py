# Write a Python program to find the common elements between two lists by converting them to sets and using the intersection operation.
list1 = [1, 2, 3, 4, 5, 3, 2] 
list2 = [3, 4, 5, 6, 7, 4, 5]
s1=set(list1)
s2=set(list2)
print(s1 & s2)