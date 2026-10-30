#Remove every single space from a given string, including spaces between words.
str1 = " P y t h o n "
def check(str1):
    str1=str1.strip()
    str1=str1.replace(" ","")
    return str1
c=check(str1)
print(c)