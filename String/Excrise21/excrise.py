#Count the frequency of every character in a string and store the results in a dictionary.
l={}
str1 = "apple"
for ch in str1:
    if ch in l:
        l[ch]+=1
    else:
        l[ch]=1
print(l)