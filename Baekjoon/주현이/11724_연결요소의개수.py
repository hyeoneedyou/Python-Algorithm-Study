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
is_visited = [0] * (n+1)

#  연결 요소 계산
def cnt(i, res, is_visited):
    if is_visited[i] == 1:
        return res, is_visited
    if len(graph[i]) == 0:
        is_visited[i] = 1
        res += 1
        return res, is_visited
    is_visited[i] = 1
    for x in graph[i]:
        cnt(x, res, is_visited)
    res += 1
    return res, is_visited


ans = 0
for i in range(1, n+1):
    ans, is_visited = cnt(i, ans, is_visited)

print(ans)