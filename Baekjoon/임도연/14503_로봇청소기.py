# 0 북, 1 동, 2 남, 3 서
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

n, m = map(int, input().split())
r, c, d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]


def clean(x, y, dirc):
    global graph

    result = 0

    while True:
        if graph[x][y] == 0:  # 현재 위치를 청소
            graph[x][y] = -1
            result += 1

        turn_d = dirc
        is_need_to_back = True
        for _ in range(4):  # 왼쪽으로 회전하며 청소가능한 공간 탐색
            turn_d = turn_d - 1 if turn_d != 0 else 3
            nx = x + dx[turn_d]
            ny = y + dy[turn_d]

            if graph[nx][ny] == 0:
                x = nx
                y = ny
                dirc = turn_d
                is_need_to_back = False
                break

        if is_need_to_back:  # 2a번 단계가 연속 네 번 실행된 경우
            nd = dirc + 2 if dirc < 2 else dirc - 2
            nx = x + dx[nd]
            ny = y + dy[nd]
            if graph[nx][ny] == 1:  # 바로 뒤쪽이 벽인 경우
                break
            x = nx
            y = ny
    return result


print(clean(r, c, d))
