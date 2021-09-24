n = int(input())
numbers = sorted(list(map(int, input().split())))
x = int(input())

result = 0
l, r = 0, n - 1
while l < r:
    t = numbers[l] + numbers[r]
    if t == x:
        result += 1
        l += 1
    elif t < x:
        l += 1
    else:
        r -= 1
print(result)