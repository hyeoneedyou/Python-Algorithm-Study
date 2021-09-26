# 못풀어서 풀이 확인함

n, m, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

check = [[False] * m for _ in range(n)]

dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
max_value = -1000000

def bfs(px, py, cnt, sum_value):
    if cnt == k:
        global max_value
        max_value = max(max_value, sum_value)
        return

    for x in range(px, n):
        for y in range(py if x == px else 0, m):
            if check[x][y]:
                continue
            flag = True
            for i in range(4):
                nx = x + dxy[i][0]
                ny = y + dxy[i][1]

                if 0 <= nx < n and 0 <= ny < m:
                    if check[nx][ny]:
                        flag = False
            if flag:
                check[x][y] = True
                bfs(x, y, cnt + 1, sum_value + graph[x][y])
                check[x][y] = False

bfs(0, 0, 0, 0)

print(max_value)