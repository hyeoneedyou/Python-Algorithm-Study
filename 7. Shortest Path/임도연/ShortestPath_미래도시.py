# 공중 미래 도시에는 1-N번까지의 회사가 서로 도로를 통해 연결되어 있다.
# 방문판매원 A는 현재 1번 회사에 위치해있으며 X번 회사에 방문해 물건을 판매하고자 한다.
# 연결된 회사는 양방향 이동이 가능하며 도르는 1만큼의 시간으로 이동할 수 있다.
# A가 1번 회사에서 출발해 K번 회사를 방문한 뒤, X번 회사로 최대한 빠르게 이동하고자 할 때 최소 시간을 계산하시오.

INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] == 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)