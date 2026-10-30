# Create an Inner Function
def outer(a,b):
    def add (a,b):
        return a+b
    ad=add(a,b)
    return ad+5
s=outer(10,20)

print(s)