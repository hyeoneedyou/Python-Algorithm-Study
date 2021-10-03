from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

# 좌 우 상 하
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if maze[ny][nx] == 0:
                continue
            if maze[ny][nx] == 1:
                maze[ny][nx] = maze[y][x] + 1
                queue.append((nx, ny))
    return maze[n-1][m-1]

print(bfs(0, 0))