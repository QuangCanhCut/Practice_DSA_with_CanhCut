s = input()

tmp = ""

for i in range(len(s)):
    if s[i].isalnum():
        tmp += s[i].lower()


def is_palindrome(l, r):
    while l < r:
        if tmp[l] != tmp[r]:
            return False
        l += 1
        r -= 1

    return True


l = 0
r = len(tmp) - 1

while l < r:
    if tmp[l] != tmp[r]:
        print(
            is_palindrome(l + 1, r)
            or is_palindrome(l, r - 1)
        )
        break

    l += 1
    r -= 1
else:
    print(True)