#  Exercise 1: Generate 3 Random Integers
import random
print("Generating 3 random integer number between 100 and 999 divisible by 5")
for i in range(3):
    print(random.randrange(100,999,5),end=" ")
