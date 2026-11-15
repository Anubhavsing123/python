# Exercise 5: Generate Random String
import random
import string
def randomst(str):
    let=string.ascii_letters
    return ''.join(random.choice(let) for i in range(str))
print(randomst(5))