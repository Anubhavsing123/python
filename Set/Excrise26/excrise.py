# Write a Python program to generate a set of squares of all even numbers from 1 to 20 using a set comprehension in a single line.
s={ i*i for i in range(1,21) if i%2==0}
print(s)