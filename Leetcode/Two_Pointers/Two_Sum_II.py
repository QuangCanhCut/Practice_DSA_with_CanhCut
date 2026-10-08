numbers = list(map(int, input().split()))
target = int(input())

ans = []

def binary_search(left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

for i in range(len(numbers) - 1):
    value = target - numbers[i]
    idx = binary_search(i + 1, len(numbers) - 1, value)
    if idx != -1:
        ans = [i + 1, idx + 1]
        break

print(ans)