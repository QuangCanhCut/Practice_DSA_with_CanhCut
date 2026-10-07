s = input()

tmp = ""

for i in range(len(s)):
    if s[i].isalnum():
        tmp += s[i].lower()

l = 0
r = len(tmp) - 1

while l < r:
    if tmp[l] != tmp[r]:
        print(False)
        break
    l += 1
    r -= 1
else:
    print(True)