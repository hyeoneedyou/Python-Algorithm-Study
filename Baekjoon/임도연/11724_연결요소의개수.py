import sys
sys.setrecursionlimit(10000)  # 재귀가 깊어지면 메모리초과가 날 수 있음

n, m = map(int, input().split())
uv = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    uv[u].append(v)
    uv[v].append(u)


def dfs(p):
    visited[p] = True
    for temp in uv[p]:
        if not visited[temp]:
            dfs(temp)


result = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        result += 1

print(result)