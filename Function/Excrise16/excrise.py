#  Use the map() function and a lambda to double every element in the list [1, 2, 3, 4, 5].
l=[1,2,3,4,5,6]
s=list(map((lambda x: x*2),l))
print(s)