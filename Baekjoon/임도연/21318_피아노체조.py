n = int(input())
music = list(map(int, input().split()))
dp = [0 for _ in range(n)]

for i in range(1, n):
    if music[i - 1] > music[i]:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = dp[i - 1]

# print(dp)
q = int(input())
result = [0 for _ in range(q)]

for i in range(q):
    _x, _y = input().split()
    x = int(_x)
    y = int(_y)

    result[i] = dp[y - 1] - dp[x - 1]

print("\n".join(map(str, result)))
