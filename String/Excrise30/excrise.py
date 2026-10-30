#Write a program to capitalize the first letter of every word in a sentence without using the built-in .title() method.
str1 = "hello world from python"
s=str1.split(" ")
print(s)
r=[]
for i in s:
    r.append(i[0].upper()+i[1:])
re=" ".join(r)
print(re)
