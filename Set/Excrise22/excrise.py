# Write a Python program to process a string and find the total number of unique words it contains, ignoring case differences.
text = "the cat sat on the mat the cat"
d=text.lower().split()
print(d)
s1=set(d)
print(s1)
print(len(s1))