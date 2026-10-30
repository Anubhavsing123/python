#Replace each special symbol with # in the following string
import string
str1 = "/*Jon is @developer & musician!!"
r="#"
pun=string.punctuation
for p in pun:
    str1=str1.replace(p,r)
print(str1)