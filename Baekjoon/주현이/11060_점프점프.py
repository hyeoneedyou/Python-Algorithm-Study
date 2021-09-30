n = int(input())
maze = list(map(int, input().split()))

dp = [1001] * n
dp[0] = 0

for i in range(0, n):
    for j in range(1, maze[i]+1):
        if i+j <= n-1:
            dp[i+j] = min(dp[i+j], dp[i] + 1)

if dp[-1] == 1001:
    print(-1)
else:
    print(dp[-1])