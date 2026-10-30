#: Given two strings, s1 and s2, create a new string from the first, middle, and last characters of each input string.

s1 = "America" 
s2 = "Japan"
middle=len(s1)//2
middle1=len(s2)//2
print(s1[0]+s2[0]+s1[middle]+s2[middle1]+s1[-1]+s2[-1])