a={"name":"Anubhav","number":1,"list":[4,5,6],"list":[1,2,34]}

# print(a["name"])
# a["name"]="Avinash"
# print(a)
# # del a["list"]
# print(a)
# a = {"name": "Anubhav"}

# print(id(a))

# a["name"] = "Rahul"

# print(id(a))
b=a["number"]
#print(b)
a["print"]="Hello world"
# print(a)
a["hello ji"]=None
#print(a,"\n")
#create new dict
# a=dict([
#     ("gi",1),
#     ("plantent","Earth")])
# print(a)
#update/cretae the key andvalue
#normal way a[keyname]=value
#use of update
a.update({"helo ji":"Doe","god":"shiv"})
# print(a)
#use setdefault it add not change the key
a.setdefault("ant","Rahul")
# print("------",a)
# print(type(a.items()))
# for i in a.items():
#     print(type(i))
# for i in a.keys():
#     print(i)
# for i in a.values():
#     print(i)
# for i,j in a.items():
#     print("\nkey:",i)
#     print("value:",j)
# print(type(a.copy()))
# print(type(a.pop("name")))
# for i in sorted(a.keys()):
#     print(i)
# for i in sorted(a.items()):
#     print(i)
c={}
# c["price"]=10.00
# c["product"]="Abue"
# print(c)
# favorite_languages = {
#  'jen': ['python', 'ruby'],
#  'sarah': ['c'],
#  'edward': ['ruby', 'go'],
#  'phil': ['python', 'haskell'],
#  }
# for i in favorite_languages.values():
#    for j in range(0,len(i)):
#       print(i[j])
#    print("\n")
sers = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },

 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location':"az"}}
for i,j in sers.items():
    for k,l in sers():
        print(k,l)
    
   