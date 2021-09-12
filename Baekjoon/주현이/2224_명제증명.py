INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

l = []
N = int(input())
for i in range(N):
    x, y = map(int, input().split('=>'))
    if x not in l:
        l.append(x)
    if y not in l:
        l.append(y)

n = len(l)
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]



for a in range(1, n + 1):
    for b in range(1, n + 1):
        if l[b-1] != 0:
            graph[a][b] = 1

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[a][b] == 1e9:
            print(0, end=" ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(1, end=" ")
    print()