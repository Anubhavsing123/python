# Create a function print_info(**kwargs) that accepts an arbitrary number of keyword arguments and prints the key-value pairs.
def print_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
print(print_info(name="Alice", age=30, city="New York"))
