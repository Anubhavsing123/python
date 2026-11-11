# Exercise 16. Check if a number is a palindrome
n=int (input("enter the number"))
t=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
if(rev==t):
    print("palidrom")
else:
    print("not palidrom")