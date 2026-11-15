# Problem Statement: Use the sys module to measure and compare the memory consumed by a list and a tuple, each holding the same one million integer elements.

import sys

data = range(1_000_000)
large_list  = list(data)
large_tuple = tuple(data)

list_size  = sys.getsizeof(large_list)
tuple_size = sys.getsizeof(large_tuple)
difference = list_size - tuple_size

print(f"List size:  {list_size:,} bytes")
print(f"Tuple size: {tuple_size:,} bytes")
print(f"Difference: {difference:,} bytes ({difference / 1024:.2f} KB)")