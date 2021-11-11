# A - B
# A - C - B

# NYY
# YNY
# YYN

N = int(input())
friend = [list(input()) for _ in range(N)] # 2차원 리스트
visited = [[0 for _ in range(N)] for _ in range(N)]

result = 0

# 나 나 너 -> ok
# 나 너 나 -> 예외처리
# 너 나 나 -> ok

for i in range(N): # A
  for j in range(N): # C
    for k in range(N): # B
      if i == k:
        continue
      if (friend[i][j] == "Y" and friend[j][k] == "Y") or friend[i][k] == "Y":
        visited[i][k] =1 # 친구

for i in visited:
  result = max(result, sum(i))

print(result)