n = int(input())
m = int(input())

visited = [False] * (n+1)
virus = []
graph = [[] for _ in range(n+1)]


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, v, visited):
    visited[v] = True
    virus.append(v)

    for  i in graph[v]:
        if not visited[i]:
            dfs(graph, i ,visited)
    return(virus)

virus = dfs(graph, 1, visited)
print(len(virus)-1)