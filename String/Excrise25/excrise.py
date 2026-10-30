#Write a program to find and print words from a string that contain both letters and numbers.
str1 = "Emma25 is Data scientist50 and AI Expert"
res=str1.split()

for ch in res:
   has1=any(c.isalpha() for c in ch)
   has2=any(c.isdigit() for c in ch)
   if has1 and has2:
      print(ch)