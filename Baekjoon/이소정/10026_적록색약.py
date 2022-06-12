import sys
sys.setrecursionlimit(10**6)

n = int(input())
table = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y): 
    visited[x][y] = 1
    now = table[x][y] # 현재 색

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n):
            if visited[nx][ny] == 0 and table[nx][ny] == now:
                dfs(nx, ny)

# 적록색약❌
normal = 0  
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            normal += 1

# 적록색약🔵
blind = 0
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if table[i][j] == 'R':
            table[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            blind += 1

print(normal, blind)