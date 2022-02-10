import sys

sys.setrecursionlimit(10 ** 6)

r, c = map(int, input().split())
input_field = [input() for _ in range(r)]

# 상하좌우
dxy = [[1, 0], [-1, 0], [0, -1], [0, 1]]

temp_sheep = 0
temp_wolf = 0

# 방문기록
record = [[0 for _ in range(c)] for _ in range(r)]
for i in range(r):
    for j in range(c):
        if input_field[i][j] == '#':
            record[i][j] = 1
        else:
            record[i][j] = 0


def search(x, y):
    if record[x][y] == 1:
        return
    record[x][y] = 1
    if input_field[x][y] == "o":
        global temp_sheep
        temp_sheep += 1
    elif input_field[x][y] == "v":
        global temp_wolf
        temp_wolf += 1

    for d in dxy:
        cx = x + d[0]
        cy = y + d[1]
        if 0 < cx < r and 0 < cy < c:
            search(cx, cy)


save_wolf = 0
save_sheep = 0
start_x = 0
start_y = 0
while True:
    temp_sheep = 0
    temp_wolf = 0
    if record[start_x][start_y] == 0:
        search(start_x, start_y)

    if temp_wolf >= temp_sheep:
        save_wolf += temp_wolf
    else:
        save_sheep += temp_sheep

    # 모두 탐색한 경우
    if start_x == r - 1 and start_y == c - 1:
        break
    else:
        if start_y == c - 1:
            start_y = 0
            start_x += 1
        else:
            start_y += 1

print(save_sheep, save_wolf)
