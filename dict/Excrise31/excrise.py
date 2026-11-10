#Exercise 31.: Write a Python program to verify whether one dictionary is a subset of another, meaning all key-value pairs of the smaller dictionary exist in the larger one.

main = {"a": 1, "b": 2, "c": 3, "d": 4} 
subset = {"a": 1, "c": 3}
issub=subset.items()<=main.items()
print(issub)