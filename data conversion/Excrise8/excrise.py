# Check whether following json is valid or invalid. If Invalid correct it
import json
def validjson(data):
    try:
        d=json.loads(data)
    except ValueError as v:
        return False
    return True
InvalidJsonData = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000 "bonus":800} } } }"""
isValid = validjson(InvalidJsonData)

print("Given JSON string is Valid", isValid)

