c=[1,2,3]
# print(c)
# print(c[0])
# print(c[1])
# print(c[2])
# print(len(c))
#revers order
print(c[::-1])
c=["Anu","Om","Sin","Avinash","Jam"]
#c[1:4] it is exclue 1 to 3 not 4 beacuse it exclude
# print(c[1:4])
# print(c[-1])
# print(c[-5:-1])
# print(c[-5:-1])
 #print(c[::2])
# #jump of 2 of each elemnt
# print(c[0:4:2])
# c[0]="Honda"
# print(c)
# c.append("Hello")
# print(c)
# c.insert(0,"Anuj")
# print(c)
# c.insert(2,"left")
# print(c)
# print(len(c))
# del c[0]
# print(c)
# print(c.pop(2))
# print(c)
# print(c.pop(0))
# print(c)
#remove item by vlaue
# d=c.remove("Jam")
# print(d)
# print(c)
cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)
# c.sort(reverse=True)
# print(c)
# d=[1,2,4,5,3,7,7,6,9,8,15,10]
# d.sort()
# print(d)
# d.sort(reverse=True)
# print(d)
#Sorting a List Temporarily with the sorted() Function
# print("original list==========",cars)
# # print("sorted list=============",sorted(cars))
# # # car=sorted(cars)
# # # print(car)
# # print("sorted list=============",sorted(cars,reverse=True))
# #Printing a List in Reverse Orderusing reversed function list change permant.
# cars.reverse()
# print(cars)
# d = [1, 2, 3, 4, 5]

# x = reversed(d)

# print(list(x))
# # motorcycles = []
# print(motorcycles[-1])
#list compersion
num=[1,2,3,4,5]
square=[ i*i for i in num]
print(square)
a=[i*i for i in range(0,11,2)]
print(a)
a=[i*i  for i in range(1,11,2)]
print(a)
# players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
# print(players[0:3],"\n")
# print(players[:4])
# print(players[2:],"\n")
# print(players[-4:])
m = ['pizza', 'falafel', 'carrot cake']
l=m[:]
print(l)
print(id(m))
print(id(l))
l=m
# print(id(l))
# print(id(m))
print(l==m)
print(l is m)
l.append("cake")
print(m)
print(l)