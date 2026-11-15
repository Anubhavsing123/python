# Exercise 9: Parse the following JSON to get all the values of a key ‘name’ within an array
s=[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]
import json
d=[]
try:
    d=json.loads(s)
except Exception as e:
    print(e)
data=[item.get('name') for item in d]
print(data)