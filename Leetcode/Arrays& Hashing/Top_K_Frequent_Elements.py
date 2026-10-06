nums = list(map(int, input().split()))
k = int(input())

freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
result = [item[0] for item in sorted_freq[:k]]

print(result)