#  Exercise 14: Accept a list of 5 float numbers
numbers = []

# Run a loop 5 times to get 5 inputs
for i in range(0, 5):
    print("Enter number at location", i, ":")
    item = float(input())
    numbers.append(item)

print("User List:", numbers)
 