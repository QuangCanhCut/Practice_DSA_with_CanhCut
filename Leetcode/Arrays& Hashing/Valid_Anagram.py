s = input().strip()
t = input().strip()

if len(s) != len(t):
    print("False")
    exit()

freq_1 = {}
freq_2 = {}

for char in s:
    if char in freq_1:
        freq_1[char] += 1
    else:
        freq_1[char] = 1

for char in t:
    if char in freq_2:
        freq_2[char] += 1
    else:
        freq_2[char] = 1

for x in freq_2:
    if x not in freq_1 or freq_1[x] != freq_2[x]:
        print("False")
        break
else:
    print("True")
