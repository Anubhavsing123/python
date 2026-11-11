# Exercise 40. Nested list search (2D matrix coordinates)
# matrix = [[10, 20], [30, 40], [50, 60]]
# target = 30
# for i in matrix:
#     for j in i:
#         if j==target:
#             print(f"{j}")

# matrix = [
#     [10, 20],
#     [30, 40],
#     [50, 60]
# ]
# target = 30

# for r_idx, row in enumerate(matrix):
#     for c_idx, val in enumerate(row):
#         if val == target:
#             print(f"Target {target} found at Row: {r_idx}, Column: {c_idx}")
#             break # Found it!

#m-3
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

target = 50

i = 0
j = len(matrix[0]) - 1

found = False

while i < len(matrix) and j >= 0:

    if matrix[i][j] == target:
        print(f"Found at row {i}, column {j}")
        found = True
        break

    elif matrix[i][j] > target:
        j -= 1

    else:
        i += 1

if not found:
    print("Element not found")
 