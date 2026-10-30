#Flatten a Deeply Nested List (Recursion)
def deep_flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            # Recursively call the function and extend the result
            result.extend(deep_flatten(item))
        else:
            result.append(item)
    return result

# Test the function
complex_list = [1, [2, [3, 4], 5], 6, [7, 8]]
flat = deep_flatten(complex_list)

print(f"Deeply Nested: {complex_list}")
print(f"Fully Flattened: {flat}")