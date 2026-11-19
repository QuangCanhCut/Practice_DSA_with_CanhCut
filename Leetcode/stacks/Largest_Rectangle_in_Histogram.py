heights = list(map(int, input().split()))

n = len(heights)
max_area = 0
stack = []

for i, height in enumerate(heights):
    start = i
    while stack and height < stack[-1][0]:
        h, j = stack.pop()
        w = i - j
        a = h * w
        max_area = max(max_area, a)
        start = j
    stack.append((height, start))

while stack:
    h, j = stack.pop()
    w = n - j
    max_area = max(max_area, h * w)

print(max_area)