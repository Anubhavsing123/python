#Write a program to generate an acronym from a given phrase (e.g., “Random Access Memory” becomes “RAM”).
str1 = "Random Access Memory"
s2=str1.split(" ")
s3=[]
print(s2)
for s in s2:
    s3.append(s[0])
print("".join(s3))
