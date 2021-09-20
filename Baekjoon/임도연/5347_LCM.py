n = int(input())
result = [0 for _ in range(n)]

for i in range(n):
    data = list(map(int, input().split()))
    data.sort()
    a, b = data[0], data[1]

    t = 0
    for j in range(a, 0, -1):
        if b % j == 0 and a % j == 0:
            t = j
            break

    result[i] = int(a * (b / t))

print("\n".join(map(str, result)))