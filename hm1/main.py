def search(nums, target):
    if target not in nums:
        return -1
    elif target in nums:
        return nums.index(target)


nums1 = [4,5,6,7,0,1,2]
nums2 = [1]
target1 = 0
target2 = 3
target3 = 0
print(search(nums1, target1))
print(search(nums1, target2))
print(search(nums2, target3))