# * * * * * * * * * * * *  : N개
#       Ai
# 

N = int(input())
jump = list(map(int, input().split()))

INF = 1e9 # 공간복잡도 생각하기
dp = [INF] * N # i까지 오는 최소 점프
dp[0] = 0 

for i in range(len(jump)): # 1
  for j in range(i+1, i+jump[i]+1):
    if j < N:
      dp[j] = min(dp[j], dp[i] + 1)

if dp[N-1] == INF:
  print(-1)
else:
  print(dp[N-1])