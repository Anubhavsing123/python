#Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1.
s1,s2 = "Ault", "Kelly"
middle=len(s1)//2
print(middle)
print(s1[0:middle]+s2+s1[middle:len(s2)+1])