# Calculate the cube of all numbers from 1 to a given number.
n=int(input())
s=0
for i in range(1,n+1):
    s=pow(i,3)
    print(s)