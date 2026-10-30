# Define a global variable global_var = 10. Write a function that successfully changes the value of this global variable to 20.
a=10
def globals_value(b):
    
    print(b)
    global a
    a=60
    
    print(a)
print(globals_value(40))


global_var = 10

def modify_variable():
    global global_var  # Access the variable from the global scope
    global_var = 20

print("Initial:", global_var)
modify_variable()
print("Modified:", global_var)