#String Rotation Check
def string(s1,s2):
    if len(s1)!=len(s2):
        return False
    com=s1+s2
    return s2 in com
s1 = "waterbottle"
s2 = "erbottlewat"
print(f"Is '{s2}' a rotation of '{s1}'? {string(s1, s2)}")
 