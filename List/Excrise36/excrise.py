#Exercise 36. Extend Nested List by Adding a Sublist
def ext(l,s):
    for i in l:
        i.append(s)
    return l
c= ext([['apple', 'banana'], ['cherry', 'date']],"elderberry")
print(c)