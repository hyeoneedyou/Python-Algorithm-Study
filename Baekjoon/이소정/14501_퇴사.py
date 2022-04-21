# 일  1  2  3  4  5  6  7
# id  0  1  2  3  4  5  6
# T  3  5  1   1  2  4  2
# P  10 20 10 20 15 40 200
# dp 45 45 45 35 15  0  0 

# dp[i] = max(dp[i+1], p[i] + dp[i + T[i]])
# 실행 X, 실행 O

n = int(input())
# #1 index와 일자 맞추기..!!
T = [0] # 0 3  5  1   1  2  4  2
P = [0] # 0 10 20 10 20 15 40 200
# #2 dp 크기 설정
dp = [0] * (n+2)

for i in range(n): # 0~6까지
    t, p= map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(n, 0, -1): # 7~1까지
    if (i + T[i]-1 > n):
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], P[i] + dp[i + T[i]])
print(dp[1])
