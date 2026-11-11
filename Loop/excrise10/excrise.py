# Print list in reverse order using a loop
# list1 = [10, 20, 30, 40, 50]
# for i in range(len(list1)-1,-1,-1):
#     print(list1[i],end=" ")
#m-2
list1 = [10, 20, 30, 40, 50]

# Use the reversed() function for clean iteration
for item in reversed(list1):
    print(item)
 