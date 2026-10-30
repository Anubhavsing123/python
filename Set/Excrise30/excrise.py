# Write a Python program to demonstrate the difference between assigning a set to a new variable with = and creating an independent copy using the .copy() method.

o={1,2,3,4,5}
r=o
r.add(7)
print("--- Assignment (=) ---")
print("original:", o)
print("ref:", r)
s=o.copy()
s.add(99)
print("\n--- Shallow copy (.copy()) ---")
print("original:", o)
print("copied:", s)
