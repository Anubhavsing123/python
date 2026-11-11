# Exercise 23. Print Alphabet pyramid (A, BB, CCC) pattern
# A 
# B B 
# C C C 
# D D D D 
# E E E E E
a=65
l=""
for i in range(5):
    l=chr(a+i)
    for j in range(0,i+1):
        print(l,end=" ")
    print("")