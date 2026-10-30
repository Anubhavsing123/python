# Create a mixed string using alternating characters
s1 = "Abc" 
s2 = "Xyz"
res=""
l= len(s1) if len(s1)>len(s2) else len(s2)
s2=s2[::-1]
for i in range(l):
    if i<len(s1):
        res+=s1[i]
    if i<len(s2):
        res+=s2[i]
print(res)
