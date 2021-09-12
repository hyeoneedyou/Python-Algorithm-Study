# 가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서,
# i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램을 작성하시오.

# 플로이드 워셜
INF = int(1e9)
n = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    d = list(map(int, input().split()))
    for j in range(1, n + 1):
        graph[i][j] = d[j - 1]

print(graph)

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()