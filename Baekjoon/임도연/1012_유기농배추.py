import sys
sys.setrecursionlimit(10**6)

t = int(input())  # 테스트 케이스 개수

for _ in range(t):
    m, n, k = map(int, input().split())  # 배추밭 가로, 세로, 배추 개수
    field = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        _y, _x = map(int, input().split())
        field[_x][_y] = 1

    dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    result = 0  # 지렁이 개수


    def go(x, y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return
        if field[x][y] == 0:
            return
        if field[x][y] == 1:
            field[x][y] = 0

        for i in range(4):
            go(x + dxy[i][0], y + dxy[i][1])


    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                result += 1
                go(i, j)
    print(result)
