# Exercise 3: PrettyPrint following JSON data
import json
sampleJson = {"key1": "value1", "key2": "value2"}
res=json.dumps(sampleJson,indent=2)
print(res)