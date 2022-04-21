
# dp[i] = max(dp[i+1], p[i] + dp[i + T[i]])
# 실행 X, 실행 O

n = int(input())
T = [] # 3  5  1   1  2  4  2
P = [] # 10 20 10 20 15 40 200
dp = [] # 10 20 10 20 15 40 200

for i in range(n): # 0~6까지
    t, p= map(int, input().split())
    T.append(t)
    P.append(p)
    dp.append(p) # 초기값 설정

for i in range(n-1, -1, -1): # 6~0까지
    if (i + T[i] > n):
        if (i == n-1):
            dp[i] = 0
        else:
            dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], P[i] + dp[i + T[i]])
print(dp[0])

# 일  1  2  3  4  5  6  7
# id  0  1  2  3  4  5  6
# T  3  5  1   1  2  4  2
# P  10 20 10 20 15 40 200
# dp 45 45 45 35 15  0  0 