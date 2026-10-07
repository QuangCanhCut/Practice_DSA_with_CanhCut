height = list(map(int, input().split()))

res = 0

for i in range(len(height)):
    max_left = max(height[:i + 1])
    max_right = max(height[i:])
    res += min(max_left, max_right) - height[i]

print(res)