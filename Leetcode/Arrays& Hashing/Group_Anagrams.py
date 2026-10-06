strs = list(map(str, input().split()))

d = {}

for i in strs:
    key = "".join(sorted(i))
    if key in d:
        d[key].append(i)
    else:
        d[key] = [i]

print(list(d.values()))
