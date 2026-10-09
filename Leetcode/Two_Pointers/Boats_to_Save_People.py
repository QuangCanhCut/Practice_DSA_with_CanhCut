people = list(map(int, input().split()))
limit = int(input())
people.sort()

l, r = 0, len(people) - 1
boats = 0

while l <= r:
    if people[l] + people[r] <= limit:
        l += 1
    r -= 1
    boats += 1

print(boats)