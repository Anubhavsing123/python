# Use the filter() function combined with a lambda to extract all even numbers from the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
num=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
e=list(filter((lambda n:n%2==0 ),num))
print(e)