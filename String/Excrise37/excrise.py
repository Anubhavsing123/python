#First Non-Repeating Character
s="swiss"
def check(s):
    d={}
    for ch in s:
        d[ch]=d.get(ch,0)+1
    
    for ch in s:
        if d[ch]==1:
            return ch
    return None
s=check(s)
print(s)