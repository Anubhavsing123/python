#Create a string made of the middle three characters
n=input("Enter the String")
middle=len(n)//2
first=middle-1
last=middle+2
t=""
for i  in range(first,last):
    t+=n[i]
print(t)
