# 캐릭터가 있는 장소는 1 * 1 크기의 정사각형으로 이뤄진 N * M 크기의 직사각형으로
# 각각의 칸은 육지 또는 바다이다.
# 캐릭터는 동서남북 중 한 곳을 바라본다.
# 각 칸은 (A, B)로 나타내며, A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수이다.
# 캐릭터는 상하좌우로 이동할 수 잇고, 바다에는 갈 수 없다.
#   1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
#   2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
#      왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 횐전만 수행하고 1단계로 돌아간다.
#   3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
#      단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
# 위 매뉴얼을 따라 캐릭터를 이동시킨 뒤, 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.

n, m = map(int, input().split())
# d = 북동남서 (0123)
x, y, d = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 상우하좌 이동 (북동남서와 매칭)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 1
rotate = 0
array[x][y] = 2

while True:
    # 네 방향 다 가보거나 바다인 경우
    if rotate > 3:
        d = d + 2 if d < 2 else d - 2
        if array[x + dx[d]][y + dx[d]] == 1: # 뒤가 바다인 경우
            break
        else: # 뒤로 한 칸 이동
            x = x + dx[d]
            y = y + dy[d]
            rotate = 0
            continue
    d = d - 1 if d != 0 else 3 # 왼쪽으로 회전
    rotate += 1
    if array[x + dx[d]][y + dy[d]] == 0:
        array[x + dx[d]][y + dy[d]] = 2
        x = x + dx[d]
        y = x + dy[d]
        result += 1
        rotate = 0

print(result)
print(array)

# # 교재 풀이
# n, m = map(int, input().split())
#
# d = [[0] * m for _ in range(n)]
# x, y, direction = map(int, input().split())
# d[x][y] = 1
#
# array = []
# for i in range(n):
#     array.append(list(map(int, input().split())))
#
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# def turn_left():
#     global direction
#     direction -= 1
#     if direction == -1:
#         direction = 3
#
# count = 1
# turn_time = 0
# while True:
#     turn_left()
#     nx = x + dx[direction]
#     ny = y + dy[direction]
#     if d[nx][ny] == 0 and array[nx][ny] == 0:
#         d[nx][ny] = 1
#         x, y = nx, ny
#         count += 1
#         turn_time = 0
#         continue
#     else:
#         turn_time += 1
#     if turn_time == 4:
#         nx = x - dx[direction]
#         ny = y - dy[direction]
#         if array[nx][ny] == 0:
#             x = nx
#             y = ny
#         else:
#             break
#         turn_time = 0
#
# print(count)