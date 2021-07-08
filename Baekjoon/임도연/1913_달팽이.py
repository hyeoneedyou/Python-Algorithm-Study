# 홀수인 자연수 N이 주어지면, 1부터 N2까지의 자연수를 달팽이 모양으로 N×N의 표에 채울 수 있다.
# N이 주어졌을 때, 표를 출력하는 프로그램을 작성하시오.
# 또한 N2 이하의 자연수가 하나 주어졌을 때, 그 좌표도 함께 출력하시오.
# 예를 들어 N=5인 경우 6의 좌표는 (4,3)이다.

n = int(input())
m = int(input())


x, y = n // 2, n // 2
mx, my = x, y
dx = [-1, 0, 1, 0] #상우하좌
dy = [0, 1, 0, -1]

pre_d = 0
d = 0 # 방향 위
array = [[0 for _ in range(n)] for _ in range(n)]
array[x][y] = 1
cnt = 2

while x != 0 and y != 0: # 2 3 3 에서 오류 수정해야함
    if array[x + dx[d - 1 if d != 0 else 3]][y + dy[d - 1 if d != 0 else 3]] == 0:
        x += dx[d]  # 보는 방향으로 이동
        y += dy[d]
        pre_d = d
        d = d + 1 if d != 3 else 0
    else:
        x += dx[pre_d]
        y += dy[pre_d]
    array[x][y] = cnt
    cnt += 1
    print(d, x, y)

for i in range(n):
    for j in range(n):
        print(array[i][j], end='')
    print()
