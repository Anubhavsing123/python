#Exercise 37. Concatenate Two Lists in a Specific Order
def Concat(l1,l2):
    return [x+y for x in l1 for y in l2]
l1 = ["Hello ", "Take "]
l2 = ["Dear", "Sir"]
res=Concat(l1,l2)
print(res)