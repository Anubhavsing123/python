# Write a program to remove all duplicate characters from a string while keeping the remaining characters in their original order.
str1 = "google"
res=[]
s=set()
for ch in str1:
    if ch not in s:
        res.append(ch)
        s.add(ch)
    
ress="".join(res)
print(ress)