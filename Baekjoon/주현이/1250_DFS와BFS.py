from collections import deque
n = int(input()) # 정점의 개수
m = int(input()) # 간선의 개수
s = int(input()) # 시작 정점

dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, dfs_visited):
    dfs_visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not dfs_visited[i]:
            dfs(graph, i, dfs_visited)


def bfs(graph, start, bfs_visited):
    queue = deque([start])
    bfs_visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not bfs_visited[i]:
                queue.append(i)
                bfs_visited[i] = True

dfs(graph, s, dfs_visited)
bfs(graph, s, bfs_visited)