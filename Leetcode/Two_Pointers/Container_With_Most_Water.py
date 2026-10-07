height = list(map(int, input().split()))

l = 0
r = len(height) - 1

max_area = 0

while l < r:
    area = (r - l) * min(height[l], height[r])
    max_area = max(max_area, area)

    if height[l] < height[r]:
        l += 1
    else:
        r -= 1

print(max_area)