# 
import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""
res=json.loads(sampleJson)
print(res['key2'])