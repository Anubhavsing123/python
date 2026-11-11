# Exercise 25. Print pyramid pattern of stars
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
n=5
for i in range(n):
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")
for k in range(n-1,0,-1):
       for j in range(k,0,-1):
            print("*",end=" ")
       print(" ")