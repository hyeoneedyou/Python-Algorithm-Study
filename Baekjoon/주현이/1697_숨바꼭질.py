from collections import deque

n, k = map(int, input().split())

if n < k:
    graph = [0] * k
else:
    graph = [0] * n
    
s = [1, -1, 2]


def bfs(x, y):
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        for i in range(3):
            nx = x + s[i]

            if graph[nx] == 0:
                graph[nx] = graph[x] + 1
                queue.append(nx)
    return graph[nx]

bfs(n,k)
