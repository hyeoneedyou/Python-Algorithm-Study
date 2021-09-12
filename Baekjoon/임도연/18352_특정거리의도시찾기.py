# 어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.
# 이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서,
# 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오.
# 또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.
# 예를 들어 N=4, K=2, X=1일 때 다음과 같이 그래프가 구성되어 있다고 가정하자.
# 이 때 1번 도시에서 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 2인 도시는 4번 도시 뿐이다.
# 2번과 3번 도시의 경우, 최단 거리가 1이기 때문에 출력하지 않는다.


# python 시간초과, pypy 맞 // 다익스트라
import heapq

INF = int(1e9)

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]  # 연결된 도로 리스트

visited = [False] * (n + 1)  # 방문 체크 리스트

distance = [INF] * (n + 1)  # 최단 거리 테이블

for _ in range(m):  # 도로 저장
    a, b = map(int, input().split())
    graph[a].append((b, 1))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(x)

if k not in distance:
    print(-1)


for i in range(n + 1):
    if distance[i] == k:
        print(i)
