N, M, V = map(int, input().split())
# 인접행렬 방식
adjacency = [[] for _ in range(N+1)]
for _ in range(M):
  v1, v2 = map(int, input().split())
  adjacency[v1].append(v2)
  adjacency[v2].append(v1)

for adj in adjacency:
  adj.sort()

# 인접 행렬 방식
def dfs(adjacency, start_node):
  visited = []
  stack = [start_node] # 시작
  while stack: # stack이 빌 때까지
    now = stack.pop()
    if now not in visited: # 방문하지 않으면
      visited.append(now)
      stack.extend(reversed(adjacency[now]))

  return visited

print(dfs(adjacency, V))