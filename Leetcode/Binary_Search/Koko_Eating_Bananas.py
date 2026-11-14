piles = list(map(int, input().split()))
h = int(input())

def min_eating_speed(piles, h):
    l, r = 1, max(piles)
    
    while l < r:
        mid = l + (r - l) // 2
        hours = sum((pile + mid - 1) // mid for pile in piles)

        if hours <= h:
            r = mid
        else:
            l = mid + 1

    return l

print(min_eating_speed(piles, h))