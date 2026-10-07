nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

nums = nums1 + nums2
nums.sort()

if len(nums) % 2 == 0:
    median = (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2
else:
    median = nums[len(nums) // 2]

print(median)