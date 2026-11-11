#Exercise 15. Find largest and smallest digit in a number
num = 75869
smallest=9
largest=0

while num>0:
    digit = num % 10
    
    # Check for new largest
    if digit > largest:
        largest = digit
    # Check for new smallest
    if digit < smallest:
        smallest = digit
        
    num = num // 10
print(largest,smallest,end=" ")