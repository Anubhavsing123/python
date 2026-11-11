# Create a program that takes an integer and prints its multiplication table from 1 to 10.
n=int(input("enter the number"))
p=1
for i in range(1,11):
    p=n*i
    print(p)