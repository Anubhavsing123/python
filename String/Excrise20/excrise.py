#Calculate the sum and average of the digits present in a string
#Given Input: str1 = "PYnative29@#8496"

#Expected Output: Sum is: 38 Average is 6.33
str1 = "PYnative29@#8496"
def check(str1):
    x=0
    c=0
    if type(str1)==str:
        for ch in str1:
            if ch.isdigit():
                x+=int(ch)
                c+=1
    return x,round(x/c,2)
c=check(str1)
print(c)
