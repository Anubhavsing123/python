#  Convert the following dictionary into JSON format
data = {"key1" : "value1", "key2" : "value2"}
import json
res=json.dumps(data)
print(res)