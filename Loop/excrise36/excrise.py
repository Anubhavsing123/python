# Exercise 36. Binary to decimal conversion using loop
binary_str = "1101"
#m-1
n=int(binary_str,2)
print(n)
#m-2

binary = "1011"
decimal = 0
power = 0

for i in range(len(binary) - 1, -1, -1):
    digit = int(binary[i])
    decimal += digit * (2 ** power)
    power += 1

print(decimal)

#m-3


binary = 1011
decimal = 0
power = 0

while binary > 0:
    digit = binary % 10
    decimal += digit * (2 ** power)
    binary //= 10
    power += 1

print(decimal)
#m-4

b="1011"
d=0
for i in b:
    d=d*2+int(i)
print(d)
