N, M = map(int, input().split())
graph = []
for i in range(N):
  graph.append(list(map(int, input())))
graph[0][0] = 1

#     상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = [[0,0]] # 0 0
visited = [[0] * M for i in range(N)] # 0 : 방문 안 한 것

while q: # q에 값이 있을 때
  # 지금 노드
  x = q[0][0] # 0
  y = q[0][1] # 0
  visited[x][y] = 1
  # 방문한 지금 노드 지우기
  del q[0]
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1 and visited[nx][ny] != 1:
      q.append([nx,ny])
      graph[nx][ny] = graph[x][y] + 1
print(graph[N-1][M-1])

# 최단거리 : bfs
# 그냥 가야되는 거 : dfs