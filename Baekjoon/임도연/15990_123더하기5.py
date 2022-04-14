t = int(input())
key_num = 1000000009
# 케이스별 끝자리 수가 1, 2, 3인 케이스를 나눠서 생각
# 3 = [2 + 1] = [1 + 2] = [3]
# dp[n][1] = dp[n-1][2] + dp[n-1][3]
# dp[n][2] = dp[n-2][1] + dp[n-2][3]
# dp[n][3] = dp[n-3][1] + dp[n-3][2]

dp = [[0 for _ in range(4)] for _ in range(100001)]
dp[1] = [0, 1, 0, 0]
dp[2] = [0, 0, 1, 0]
dp[3] = [0, 1, 1, 1]

for i in range(4, 100001):
    dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % key_num
    dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % key_num
    dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % key_num

for _ in range(t):
    n = int(input())
    print(sum(dp[n]) % key_num)
