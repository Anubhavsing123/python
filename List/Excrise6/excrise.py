#Count Even and Odd Numbers
n=[10, 21, 4, 45, 66, 93, 11]
even=0
odd=0
for i in n:
    if i %2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)