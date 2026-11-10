#Exercise 26. : Write a Python program to count the frequency of each word in a string, treating words case-insensitively so that “The” and “the” are counted as the same word.

text = "the cat sat on the mat the cat"
s=text.split(" ")
print(s)
d={}
for i in s:
    d[i]=d.get(i,0)+1

print(d)