# Exercise 8. Percentage display
num = int(input("Enter numerator: "))
den = int(input("Enter denominator: "))

percentage = (num / den) * 100

# Using f-string for precision and adding the '%' literal
print(f"The result is: {percentage:.2f}%")