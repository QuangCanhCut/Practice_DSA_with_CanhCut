a = list(map(int, input().split()))

d = {}

for i in range (len(a)):
    if a[i] in d:
        print("True")
        break
    d[a[i]] = i
else:
    print("False")