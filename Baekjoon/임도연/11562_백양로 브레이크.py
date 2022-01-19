INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    u, v, b = map(int, input().split())
    graph[u][v] = 0
    graph[v][u] = 1 if b == 0 else 0

# 1 -> 2 <-> 3 -> 4
for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0
                continue
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

k = int(input())

for _ in range(k):
    s, e = map(int, input().split())
    print(graph[s][e])
