# Write a code to generate 100 random lottery tickets and pick two lucky tickets from it as a winner.

import random
l=[]
for i in range(100):
    l.append(random.randrange(1000000000, 9999999999))
winner=random.sample(l,2)
print(winner)