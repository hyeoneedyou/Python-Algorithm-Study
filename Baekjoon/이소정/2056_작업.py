# time, 선행관계 작업수, 작업번호
# 5 0
# 1 1 1
# 3 1 2

n = int(input())
dp = [0] * (n + 1)

for i in range(1, n+1):
  arr = list(map(int, input().split()))
  for j in arr[2:]: # 개수만큼  for문 돌려서  dp 확인
    dp[i] = max(dp[i], dp[j] + arr[0])
print(max(dp))