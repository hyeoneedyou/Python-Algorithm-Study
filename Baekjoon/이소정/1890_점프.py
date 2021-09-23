# 1 _ _ _  
# _ _ _ _    
# _ _ _ _    
# _ _ _ *    
# dp[y][x]
# 오른쪽 or 아래쪽
# 방향 바꾸면 안됨
# 0은 종착점

N =  int(input()) # 판의 크기
table = [list(map(int, input().split())) for _ in range(N)]
# dp = [[0] * N] * N
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1 # 시작지점 1

for y in range(N): # 행
  for x in range(N): # 열
    if table[y][x] != 0 and dp[y][x] != 0:
      # 아래로 이동 가능한 경우
      if y + table[y][x] <= N-1: # 넘어가면 안됨
        dp[y+table[y][x]][x] += dp[y][x]
      # 오른쪽으로 이동 가능한 경우
      if x + table[y][x] <= N-1: # 넘어가면 안됨
        dp[y][x+table[y][x]] += dp[y][x]

print(dp[-1][-1])
# print(dp)

# dp         table
# 1 0 1 0    2 3 3 1
# 0 0 0 0    1 2 1 3
# 1 1 0 1    1 2 3 1
# 1 0 1 3    3 1 1 0
# (y,x)