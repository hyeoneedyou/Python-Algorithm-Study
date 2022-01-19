import pprint

n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

# 같은 건물
for i in range(1, n+1):
  graph[i][i] = 0

# graph 그리기
for _ in range(m):
  u, v, b = map(int, input().split())
  if b == 1: # 양방향
    graph[u][v] = 0
    graph[v][u] = 0
  elif b== 0: # 단방향
    graph[u][v] = 1


# i -> j
# i -> k -> j
for i in range(1, n+1):
  for j in range(1, n+1):
    for k in range(1, n+1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

k = int(input())
for _ in range(k):
  s, e = map(int, input().split())
  print(graph[s][e])

pprint.pprint(graph)
