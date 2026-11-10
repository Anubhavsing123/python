magicians = ['alice', 'david', 'carolina']
# for i in magicians:
#     print(i)
# for i in range(0,7):
#     print(i)
# print("\n")
# for i in range(1,10,2):
#     print(i)
# print("\t")
# for i in range(2,11,2):
#     print(i)
l=list(range(1,7))
print(l)
s=[]
for i in magicians:
    s.append(i)
print(s)
l=[]
for i in range(1,11):
    v=i**2
    l.append(v)
print(l)
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(type(id(digits)))
print(min(digits))
print(max(digits))
print(sum(digits))
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(type(players[:3]))
for i in players[:3]:
    print(type(i))
    print(i)
for i in digits[:3]:
    print(type(i))
    print(i)