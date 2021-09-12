# 상자의 개수
# 상자의 크기

# 상자번호
# 1 6 2 5 7 3 5 6
# dp
# [1, 2, 2, 3, 4, 3, 4, 5]
# 본인 상자보다 작아야하고, 여러개 일 경우 배열 큰 것

n = int(input())
box_list = list(map(int, input().split()))

dp = [1] * n
# [1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, n): # 1 부터 7까지, 0은 자동으로 1이니까
  for j in range(0, i): # i 이전까지 검사
    # box_list[j]가 box_list[i]보다 숫자가 작아야 하고, 작은 것이 어려개라면 dp가 큰 것을 선택
    if box_list[j] < box_list[i] :
      dp[i] = max(dp[j] + 1, dp[i]) # 새로운 것 vs 기존의 것(1)
    # else : 그냥 자동으로 1
print(max(dp))