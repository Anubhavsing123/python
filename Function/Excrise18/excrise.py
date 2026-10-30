# Write a function apply_operation(func, x, y) that takes another function (func) and two numbers (x, y) as arguments. It should return the result of calling func(x, y). Show how this works by passing in different operations like addition and multiplication.

def apply_op(func,x,y):
    return func(x,y)
def add(a,b):
    return a+b
def mul(a,b):
    return a*b
res=apply_op(add,3,2)
print(res)
res=apply_op(mul,2,3)

print(res)