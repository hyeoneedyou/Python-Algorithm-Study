# 10 X 8
# 1 1 * * * * * * * * 
# * 1 * * * * * * * * 
# * * * * 1 * * * * * 
# * * * * 1 * * * * * 
# * * 1 1 * * * 1 1 1 
# * * * * 1 * * 1 1 1 
# * * * * * * * 1 1 1 
# * * * * * * * * * * 

def make_graph(M, N, K):
  graph = [[0] * M for _ in range(N)]
  for _ in range(K):
    X, Y = map(int, input().split())
    graph[Y][X] = 1
  return graph

def dfs(X, Y):
  # 상 하 좌 우
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]

  for i in range(4):
    nx = X + dx[i]
    ny = Y + dy[i]

    if nx < 0 or nx>=M or ny<0 or ny>=N:
      return False

    if graph[nx][ny] == 1:
      graph[nx][ny] == 0
      dfs(nx, ny)
      return True

T = int(input())
for _ in range(T):
  M, N, K = map(int, input().split())
  graph = make_graph(M, N, K)
  cnt = 0
  for i in range(N):
    for j in range(M): 
      if graph[i][j] == 1: 
        dfs(i, j) 
        cnt += 1

print(cnt)

