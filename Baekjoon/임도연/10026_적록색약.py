import sys
sys.setrecursionlimit(10**6)

n = int(input())
drawing = [list(input()) for _ in range(n)]

red_green_diff = 0  # 적록색약이 아닌 사람
red_green_same = 0  # 적록색약인 사람

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, color):
    global visited

    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if visited[nx][ny] == 1:
            continue

        if drawing[nx][ny] == color:
            dfs(nx, ny, color)


visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] != 1:
            dfs(i, j, drawing[i][j])
            red_green_diff += 1

for i in range(n):
    for j in range(n):
        if drawing[i][j] == "R":
            drawing[i][j] = "G"

visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] != 1:
            dfs(i, j, drawing[i][j])
            red_green_same += 1

print(red_green_diff, red_green_same)