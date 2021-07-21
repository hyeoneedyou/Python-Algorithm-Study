import sys
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
parent_node = [0] * (n + 1)


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            parent_node[i] = v
            dfs(graph, i, visited)


array = [False] * (n + 1)
dfs(graph, 1, array)

for i in range(2, n + 1):
    print(parent_node[i])
