# 310
# 50 100 200
# 40 70 150

n, t = map(int, input().split())

times = []
scores = []
dp = [[0] * t  for _ in range(n+1)]

#     0 1 2 3 4 50 ...   100 ... 200 310시간
#     - - - - - - - - - - - - - - - - - -
# 1단 0 0 0     40 40 40 40  40 ...
# 2단 0 0 0              70  70 ...
# 3단 0 0 0                      150 150 ...

for _ in range(n):
    k, s = map(int, input().rsplit())
    times.append(k)
    scores.append(s)

for i in range(1, n+1): # 1, 2 ... 문제
    for j in range(t+1): # 0시간~ t시간 공부
        if times[i] <= j :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-times[i]] + scores[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][t])