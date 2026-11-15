# Problem Statement: Write a Python program to extract a specific portion of a tuple using slice notation.
#m-1
# numbers = (10, 20, 30, 40, 50, 60, 70)
# res=[]
# for i in range(1,4):
#     res.append(numbers[i])
# r=tuple(res)
# print(r)
#m-2
# numbers = (10, 20, 30, 40, 50, 60, 70)
# res=tuple(numbers[i] for i in range(1,5))
# print(res)
#m-3
numbers = (10, 20, 30, 40, 50, 60, 70)

result = numbers[1:4]

print(result)