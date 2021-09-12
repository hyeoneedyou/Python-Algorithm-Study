# N개의 도시가 있고 각 도시에서 메시지를 보낼때는 단방향으로 전송된다.
# C라는 도시에서 위급상황이 발생해 최대한 많은 도시로 메시지를 보내려할 때 도시 C에서 보낸 메시지를 받는 도시 개수와 총 시간을 계산하시오

import heapq
import sys

input = sys.stdin.readline()
INF = int(1e9)  # 10억

n, m, start = map(int, input().split())

graph = [[] for i in range(n + 1)]  # 각 노드에 연결된 노드에 대한 정보가 담김

visited = [False] * (n + 1)  # 방문 체크 리스트

distance = [INF] * (n + 1)  # 최단 거리 테이블

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


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


dijkstra(start)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)