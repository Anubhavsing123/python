# Exercise 24. Hollow square pattern

for i in range(0,6):
    for j in range(0,6):
        if i==0 or i==5 or j==0 or j==5:
            print("*",end=" ")
        else:
         print(" ",end=" ")
    print()