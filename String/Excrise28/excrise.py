#Write a program to check if two strings are anagrams (formed by rearranging the letters of another, such as “listen” and “silent”).
s1 = "listen"
s2 = "silent"
s1=sorted(s1)
s2=sorted(s2)
if s1==s2:
    print("Done")
else:
    print("not ok")