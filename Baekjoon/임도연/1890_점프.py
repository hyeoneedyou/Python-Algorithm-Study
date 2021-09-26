import sys
sys.setrecursionlimit(10**6)

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(n)] for _ in range(n)]


def dfs(x, y):
    if x == n - 1 and y == n - 1:
        return 1
    if x >= n or y >= n or array[x][y] == 0:
        return 0

    if visited[x][y] != 0:
        return visited[x][y]

    jump = array[x][y]
    visited[x][y] = dfs(x + jump, y) + dfs(x, y + jump)
    return visited[x][y]


print(dfs(0, 0))