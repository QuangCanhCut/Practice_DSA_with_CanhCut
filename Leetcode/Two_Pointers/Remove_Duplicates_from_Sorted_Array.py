nums = list(map(int, input().split()))

l = 0
for r in range(1, len(nums)):
    if nums[r] != nums[l]:
        l += 1
        nums[l] = nums[r]

print(l + 1)