#Exercise 15. : Write a Python program to count how many times each character appears in a given string, storing the results in a dictionary.
text = "hello world"
fre={}
for ch in text:
    fre[ch]=fre.get(ch,0)+1
print(fre)