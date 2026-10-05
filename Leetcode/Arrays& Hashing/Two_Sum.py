a = list(map(int, input().split()))

target = int(input())

d = {}

for i in range (len(a)):
    find = target - a[i]
    if find in d:
        print(d[find], i)
        break
    d[a[i]] = i
