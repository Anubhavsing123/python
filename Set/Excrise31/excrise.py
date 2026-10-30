#  Write a Python program to compare the time taken to check whether an item exists in a large list versus a large set, and observe the performance difference.
import time
l=list(range(10000))
s=set(range(10000))
t=99999
start = time.time()
res= t in l
list_time = time.time() - start


start = time.time()
result = t in s
set_time = time.time() - start

print(f"List lookup time:  {list_time:.6f} seconds")
print(f"Set lookup time:   {set_time:.6f} seconds")
