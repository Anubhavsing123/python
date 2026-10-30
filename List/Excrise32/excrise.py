#32 Check if List is Sorted
l=[10, 20, 30, 25, 40]
def cehk(l):
    return all(l[i] <=l[i+1] for i in range(len(l)-1))
print(cehk(l))