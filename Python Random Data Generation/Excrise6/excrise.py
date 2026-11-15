# Exercise 6: Generate Random Password
import random
import string
def password():
    password_create=string.ascii_letters+string.digits+string.punctuation
    password_ma=random.sample(password_create,6)
    password_ma+=random.sample(string.ascii_uppercase,2)
    password_ma+=random.choice(string.digits)
    password_ma+=random.choice(string.punctuation)
    password_list=list(password_ma)
    random.SystemRandom().shuffle(password_list)
    password_ma="".join(password_list)
    return password_ma
print(password())