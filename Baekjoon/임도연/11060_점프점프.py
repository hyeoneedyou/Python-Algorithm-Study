n = int(input())
maze = list(map(int, input().split()))

dp = [1001] * (n + 1)
dp[0] = 0
dp[1] = 0

for i in range(1, n + 1):
    for j in range(1, maze[i - 1] + 1):
        if i + j <= n:
            dp[i + j] = min(dp[i + j], dp[i] + 1)
print(dp)

if n == 1:
    print(int(bool(maze[0])))
elif dp[n] == 1001:
    print(-1)
else:
    print(dp[n])