# 최단 경로(Shortest Path)
- 가장 짧은 경로를 찾는 알고리즘
- 노드와 간선을 이용해 그래프로 표현
- 최단 경로를 모두 출력하는 문제보다는 단순히 최단거리를 출력하도록 요구하는 문제가 많이 출제됨
- `다익스트라 최단 경로 알고리즘`, `플로이드 워셜`, `벨만 포드 알고리즘`로 나뉘며, 앞의 두 유형만 알아도 코딩 테스는 문제 없음
- 그리디 알고리즘 및 다이나믹 프로그래밍 알고리즘의 한 유형

## 다익스트라 최단 경로 알고리즘
- 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각가의 최단 경로를 구해주는 알고리즘
- `음의 간선`이 없을 때 정상적으로 동작
    - 음의 간선이란 0보다 작은 값을 가지는 간선
    - GPS 소프트웨어의 기본 알고리즘
- 그리디 알고리즘으로 분류(매번 가장 비용이 적은 노드를 선택해서 임의의 과정을 반복)
### 원리
1. 출발 노드를 설정
2. 최단 거리 테이블을 초기화
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
5. 위 과정에서 3번과 4번을 반복

- 각 노드에 대한 현재까지의 최단 거리 정보를 항상 1차원 리스트에 저장하며 리스트를 계속 갱신

- 무한 값 대입할 때 `int(1e9)`

- 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것
### 방법 1. 간단한 다익스트라 알고리즘
- O(V^2)
- 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인(순차 탐색)
```python
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
```
### 방법 2. 개선된 다익스트라 알고리즘
- O(ElogV)
- `힙(Heap)`자료구조를 이용해 특정노드까지의 최단 거리에 대한 정보를 힙에 담아서 처리하므로 출발 노드로
부터 가장 거리가 짧은 노드를 더욱 빠르게 찾을 수 있음

#### 힙
- 우선순위 큐(Priority Queue)를 구현하기 위해 사용하는 자료구조 중 하나
- `우선순위 큐`: 우선순위가 가장 높은 데이터를 가장 먼제 삭제
- `PriorityQueue` 또는 `heapq`(더 빠름) 라이브러리 사용
- 우선순위 값을 표현할 때는 일반적으로 정수형 자료형의 변수가 사요됨
- 우선순위 큐 라이브러리에 데잍의 묶음을 넣으면, 첫번째 원소를 기준으로 우선순위를 설정
- `최소 힙(Min Heap)`: 값이 낮은 데이터가 먼저 삭제
- `최대 힙(Max Heap)`: 값이 큰 데이터가 먼저 삭제
- 파이썬의 우선순위 큐 라이브러리는 최소 힙에 기반
- 최소 힙을 최대 힙처럼 사용하기 위해 일부러 우선순위에 해당하는 값에 음수 부호를 붙여서 넣었다가,
나중에 우선순위 큐에서 꺼낸 다음에 다시 음수 부호를 붙여서 원래의 값으로 돌리는 방식



- 최단 거리를 저장하기 위한 1차원 릿트(최단 거리 테이블)는 그대로 이용하고,
현재 가장 가까운 노드를 저장하기 위한 목적으로만 우선순위 큐를 추가로 이용
```python

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
```

## 플로이드 워셜 알고리즘(Floyd-Warshall Algorithm)
- 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우
- O(N^3)
- 노드의 개수가 N개일 때 알고리즘 상으로 N번의 단계를 수행하며,
단계마다 O(N^2)의 연산을 통해 현재 노드를 거쳐가는 모든 경로를 고려
- 2차원 리스트에 최단 거리 정보를 저장
- 다이나믹 프로그래밍
```python
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

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
            print("INFINITY", end=" ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=" ")
    print()
```