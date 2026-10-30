# Count the occurrences of each word in a string and store the result in a dictionary.
str1 = "apple banana apple cherry banana apple"
st=str1.split(" ")
d={}
for s in st:
    d[s]=d.get(s,0)+1
print(d)