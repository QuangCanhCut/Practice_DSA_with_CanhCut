words = list(map(str, input().split()))
k = int(input())

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
result = [item[0] for item in sorted_freq[:k]]

print(result)