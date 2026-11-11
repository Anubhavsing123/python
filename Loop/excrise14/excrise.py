#Reverse an integer number
n=76542
rev=0
while n>0 :
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)