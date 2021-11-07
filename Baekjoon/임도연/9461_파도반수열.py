c = int(input())
n = [int(input()) for _ in range(c)]

dp = [0] * 101
dp[0] = 1
dp[1] = 1
dp[2] = 1
for i in range(3, max(n)):
    dp[i] = dp[i - 3] + dp[i - 2]

for i in n:
    print(dp[i - 1])