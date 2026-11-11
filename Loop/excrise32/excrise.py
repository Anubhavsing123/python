#Exercise 32. List Rotation: Rotate elements left by k positions
nums = [1, 2, 3, 4, 5]
k = 2
for i in range(k):
    first=nums.pop(0)
    nums.append(first)
print(nums)
#m2
l=nums[:k]+ nums[k:]
print(l)

#m-3
nums = [1, 2, 3, 4, 5]
k = 2

n = len(nums)
k = k % n

nums[:k] = reversed(nums[:k])
nums[k:] = reversed(nums[k:])
nums.reverse()

print(nums)
nums = [1, 2, 3, 4, 5]
k = 2

def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

n = len(nums)
k = k % n

reverse(nums, 0, k - 1)
reverse(nums, k, n - 1)
reverse(nums, 0, n - 1)
