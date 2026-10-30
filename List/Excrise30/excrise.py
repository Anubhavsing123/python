#Exercise 30. Find All Common Elements Between Three Lists
a=[1, 5, 10, 20]
b= [6, 7, 20, 80, 100]
c= [3, 4, 15, 20, 30, 70, 80]
s1=set(a)
s2=set(b)
s3=set(c)

l=list(s1 &s2 & s3)
       
print(l)