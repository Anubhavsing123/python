# Exercise 19. Armstrong Number Check
n=153
r=0
temp=n
while n>0:
    digit=n%10
    r=r+digit**3
    n//=10
if temp == r:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")