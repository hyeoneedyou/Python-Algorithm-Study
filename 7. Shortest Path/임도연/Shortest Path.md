# 최단 경로
가장 짧은 경로를 찾는 알고리즘

간선으로 연결된 노드로 구성
-> 다익스트라 최단 경로 알고리즘, 플로이드 워셜 알고리즘, 벨만 포드 알고리즘 등
## 다익스트라 최단 경로 알고리즘
**다익스트라 알고리즘** : 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
-> 음의 간선이 없어야 한다 (GPS SW의 기본 알고리즘으로 채택되곤 함)

다익스트라 알고리즘 원리
> 1. 출발 노드를 설정한다.
> 2. 최단 거리 테이블을 초기화한다.
> 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
> 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
> 5. 위 과정에서 3, 4번을 반복한다.

구현 방법
- 구현하기 쉽지만 느리게 동작하는 코드 : 방문하지 않은 노드중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 리스트의 모든 원소를 순차탐색
```python
import sys
input = sys.stdin.readline()
INF = int(1e9)  # 10억

n, m = map(int, input().split())
start = int(input())  # 시작 노드

graph = [[] for i in range(n + 1)]  # 각 노드에 연결된 노드에 대한 정보가 담김

visited = [False] * (n + 1)  # 방문 체크 리스트

distance = [INF] * (n + 1)  # 최단 거리 테이블

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def get_smallest_node():  # 아직 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드의 번호 리턴
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
```
시간 복잡도 : O(V^2)

- 구현하기에 조금 더 까다롭지만 빠르게 동작하는 코드 : 현재 가장 가까운 노드를 저장하기 위한 목적으로만 우선순위 큐를 추가로 이용
```python
import heapq
import sys
input = sys.stdin.readline()
INF = int(1e9)  # 10억

n, m = map(int, input().split())
start = int(input())  # 시작 노드

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
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
```
시간 복잡도 : O(ElogV)

## 플로이드 워셜 알고리즘
**플로이드 워셜 알고리즘** : 모든 지점에서 다른 모든 지전까지의 최단 경로를 모두 구해야하는 경우에 사용하는 알고리즘

점화식 : Dab = min(Dab, Dak + Dkb)

```python
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

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
```
시간 복잡도 : O(N^3)

## [문제] 미래도시
> 공중 미래 도시에는 1-N번까지의 회사가 서로 도로를 통해 연결되어 있다.
> 방문판매원 A는 현재 1번 회사에 위치해있으며 X번 회사에 방문해 물건을 판매하고자 한다.
> 연결된 회사는 양방향 이동이 가능하며 도르는 1만큼의 시간으로 이동할 수 있다.
> A가 1번 회사에서 출발해 K번 회사를 방문한 뒤, X번 회사로 최대한 빠르게 이동하고자 할 때 최소 시간을 계산하시오.

```python
# 교재 풀이
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
```
-> n의 점위가 100이하이기 때문에 플로이드 워셜 알고리즘을 이용해도 빠르게 풀 수 있다. 

## [문제] 전보
> N개의 도시가 있고 각 도시에서 메시지를 보낼때는 단방향으로 전송된다.
> C라는 도시에서 위급상황이 발생해 최대한 많은 도시로 메시지를 보내려할 때 도시 C에서 보낸 메시지를 받는 도시 개수와 총 시간을 계산하시오


```python
# 교재 풀이
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
```
-> 우선순위 큐를 이용한 다익스트라 알고리즘