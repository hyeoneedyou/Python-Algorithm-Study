# 여행가 A는 N * N 크기의 정사각형 공간 위에 서 있다.
# 이 공간은 1 * 1 크기의 정사각형으로 나누어져 있다.
# 가장 왼쪽 위 좌표는 (1, 1)이며 가장 오른쪽 아래 좌표는 (N, N,)이다.
# 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며 시작은 항상 (1, 1)이다.

n = int(input())
plan = input().split()
dic = {'U':0, 'D':1, 'L':2, 'R':3}
x, y = 1, 1
# U, D, L, R 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(len(plan)):
    px = d[0] + dx[dic[plan[i]]]
    py = d[1] + dy[dic[plan[i]]]
    if px < 1 or px > n or py < 1 or py > n:
        continue
    x, y = px, py

print(x, y)

# # 교재 풀이
# n = int(input())
# x, y = 1, 1
# plans = input().split()
#
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']
#
# for plan in plans:
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     x, y = nx, ny
#
# print(x, y)