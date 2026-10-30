#Remove special symbols/punctuation from a string
str1 = "/*Jon is @developer & musician!!"
res=""
for ch in str1:
    if ch.isalnum() or ch.isspace():
        res+=ch
print(res,end="")
