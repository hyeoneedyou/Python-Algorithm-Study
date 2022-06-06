# 0(x 증가), 1(y 감소), 2(x 감소), 3(y 증가) => 사계방향
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())

dots = []

for _ in range(n):
    x, y, d, g = map(int, input().split())

    directions = [d]
    for _ in range(g):
        for i in range(len(directions) - 1, -1, -1):
            new_direction = directions[i] + 1 if directions[i] < 3 else 0
            directions.append(new_direction)

    if [x, y] not in dots:
        dots.append([x, y])
    for direct in directions:
        x += dx[direct]
        y += dy[direct]
        if 0 <= x <= 100 and 0 <= y <= 100:
            if [x, y] not in dots:
                dots.append([x, y])

field = [[0 for _ in range(101)] for _ in range(101)]

for [x, y] in dots:
    field[y][x] = 1

result = 0
for i in range(100):
    for j in range(100):
        if field[i][j] == 1 and field[i + 1][j] == 1 and field[i][j + 1] == 1 and field[i + 1][j + 1]:
            result += 1

print(result)
