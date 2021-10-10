import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
# 연결된 정점 저장
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
#  체크 여부
visited = [0] * (n+1)


#  연결 요소 계산
def dfs(p):
    visited[p] = True
    for x in graph[p]:
        if not visited[x]:
            dfs(x)


ans = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        ans += 1

print(ans)

