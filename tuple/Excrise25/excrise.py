# Problem Statement: Write a Python program that experiments with using tuples as dictionary keys. Demonstrate why a fully immutable tuple like (1, 2) works as a key, while a tuple containing a mutable object like (1, [2]) raises a TypeError.

d = {}

# Fully immutable tuple: works as a key
try:
    d[(1, 2)] = "immutable tuple"
    print(f"(1, 2) as key: success, value = \"{d[(1, 2)]}\"")
except TypeError as e:
    print(f"(1, 2) as key: TypeError - {e}")

# Tuple containing a list: raises TypeError
try:
    d[(1, [2])] = "tuple with list"
    print(f"(1, [2]) as key: success, value = \"{d[(1, [2])]}\"")
except TypeError as e:
    print(f"(1, [2]) as key: TypeError - {e}")

# Demonstrating hash() directly
print("\nhash((1, 2))  =", hash((1, 2)))
try:
    print("hash((1, [2])) =", hash((1, [2])))
except TypeError as e:
    print(f"hash((1, [2])): TypeError - {e}")