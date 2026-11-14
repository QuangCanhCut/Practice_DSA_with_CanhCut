nums = list(map(int, input().split()))

def find_min(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2

        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid - 1

    return nums[l]

print(find_min(nums))