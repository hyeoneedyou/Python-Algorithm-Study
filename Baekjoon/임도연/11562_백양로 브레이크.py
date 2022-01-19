import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
road = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

# 건물 사이의 길에 대한 정보 저장
for _ in range(m):
    u, v, b = map(int, input().split())
    road[u][v] = 1
    if b == 1:
        road[v][u] = 1

k = int(input())
questions = [list(map(int, input().split())) for _ in range(k)]

# 1 -> 2 <=> 3 -> 4


def find_road(path, temp, goal, change=0):
    if temp == goal:
        print(change)
        return

    for i in range(1, n + 1):
        if path[temp][i] == 0:
            path[temp][i] += 1
            if road[temp][i] == 1:
                find_road(path, i, goal, change)
            elif road[temp][i] == 0 and road[i][temp] == 1:
                find_road(path, i, goal, change + 1)


for q in questions:
    start, end = q

    temp_path = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    find_road(temp_path, start, end)