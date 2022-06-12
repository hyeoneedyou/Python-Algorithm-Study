import sys
sys.setrecursionlimit(10**6)

n = int(input())
drawing = [input() for _ in range(n)]

red_green_diff = 0  # 적록색약이 아닌 사람
red_green_same = 0  # 적록색약인 사람

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0] * n for _ in range(n)]
rgs = False


def dfs(x, y, color, is_rgs):
    global visited, rgs

    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if visited[nx][ny] == 1:
            continue

        if (color == "R" and drawing[nx][ny] == "G") or (color == "G" and drawing[nx][ny] == "R"):
            dfs(nx, ny, color, True)
            rgs = True
        elif drawing[nx][ny] == color:
            dfs(nx, ny, color, is_rgs)


for i in range(n):
    for j in range(n):
        if visited[i][j] != 1:
            rgs = False
            dfs(i, j, drawing[i][j], False)
            print(visited, rgs)
            if rgs:
                red_green_diff += 1
            red_green_diff += 1
            red_green_same += 1

print(red_green_diff, red_green_same)