#Exercise 33. : Write a Python program to find the key in a dictionary whose associated list value has the greatest number of elements.
data = {"fruits": ["apple", "banana", "cherry"], "vegs": ["carrot"], "grains": ["rice", "wheat"]}
s=max(data.items(),key= lambda x: len(x[1]))[0]
print(s)