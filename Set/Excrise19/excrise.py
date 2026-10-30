#. Write a Python program to remove and return an arbitrary element from a set using pop(), and handle the KeyError that occurs when the set is empty.
s = {100, 200, 300}
p=s.pop()
print(p)

s=set()
try:
    s.pop()
except KeyError as e:
    print(e)
    
