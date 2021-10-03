from collections import deque
n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

# 아래, 오른쪽, 위, 왼쪽
dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dxy[i][0]
            ny = y + dxy[i][1]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    return maze[n - 1][m - 1]


print(bfs(0, 0))


n, m = map(int, input().split())
maze = [input() for _ in range(n)]

# 아래, 오른쪽, 위, 왼쪽
dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
result = []


def dfs(x, y, path, go):
    if maze[x][y] == '0' or go[x][y]:
        return

    if x == n - 1 and y == m - 1:
        return result.append(path)

    go[x][y] = True

    for i in range(4):
        nx = x + dxy[i][0]
        ny = y + dxy[i][1]
        if 0 <= nx < n and 0 <= ny < m:
            dfs(nx, ny, path + 1, go)


array = [[False for _ in range(m)] for _ in range(n)]
dfs(0, 0, 1, array)

print(min(result))
