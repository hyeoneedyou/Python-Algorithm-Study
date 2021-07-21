# 자료구조 기초
**탐색** : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정

**자료구조** : 데이터를 표현하고 관리하고 처리하기 위한 구조
- 스택과 큐는 자료구조의 기초 개념으로 삽입, 삭제로 구성된다.

## 스택
**후입선출(Last In First Out) 구조**
```python
stack = []

stack.append(5)
stack.append(1)
stack.pop()
stack.append(3)

print(stack)  # [5, 3]
```
별도의 라이브러리를 사용할 필요 없이 리스트의 `append()`와 `pop()` 메서드를 이용하면 스택 자료구조와 동일하게 동작한다.

## 큐
**선입선출(First In First Out) 구조**
```python
from collections import deque

queue = deque()

queue.append(5)
queue.append(1)
queue.popleft()
queue.append(3)

print(queue)  # deque([3, 1])
```

`collections 모듈`에서 제공하는 `deque 자료구조`를 활용할 수 있다.
데이터 삽입, 삭제 속도가 리스트에 비해 효율적이다.
`list(queue)`를 이용하면 리스트 자료형이 반환된다.

## 재귀함수
자기 자신을 다시 호출하는 함수
```python
def recursive_function():
    print('재귀함수 호출')
    recursive_function()

recursive_function()
```

재귀함수는 **종료 조건**을 명시해서 최대 깊이를 초과하지 않도록 주의해야한다.
재귀함수는 내부적으로 스택 자료구조와 동일하기 때문에 스택을 활용하는 알고리즘을 간편하게 구현할 수 있다.

```python
# 팩토리얼 예제
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

print(factorial_recursive(5))  # 120
```

# 그래프
- 그래프는 노드와 간선으로 표현되며 이때 노드를 정점이라고도 말한다.

- 그래프 탐색이란 하나의 노드를 시작으로 다수의 노드를 방문하는 것을 말한다.
 
 
그래프 표현 방식
- 인접 행렬 : 2차원 배열로 그래프의 연결 관계를 표현하는 방식
```python
INF = 999999999  # 무한의 비용 선언 => 연결되어 있지 않은 노드끼리의 비용

graph = [
       [0, 7, 5],
       [7, 0, INF],
       [5, INF, 0]
]

print(graph)
```

- 인접 리스트 : 리스트로 그래프의 연결 관계를 표현하는 방식
```python
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))
# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0,7))
# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0,5))

print(graph)
```

> 인접 리스트 방식은 연결된 정보만을 저장하기 때문에 메모리를 효율적으로 사용하지만 특정 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느리다.

# DFS
**DFS(Depth-First Search)** : 깊이 우선 탐색, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘.

동작 과정
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
1. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있다면 그 인접 노드를 스택에 넣고 방문처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
1. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

_DFS는 관행적으로 번호가 낮은 순서부터 처리하도록 구현하는 편이다._

```python
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)  # 1 2 7 6 8 3 4 5
```

# BFS
**BFS(Breadth First Search)** : 너비 우선 탐색, 가까운 노드부터 탐색하는 알고리즘

동작 과정
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
1. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
1. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

```python
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)  # 1 2 3 8 7 4 5 6
```

_일반적인 경우 실제 수행 시간은 DFS보다 좋은 편이다._

## [문제] 음료수 얼려 먹기
> N * M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
> 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
> 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.

-> dfs를 이용해 상하좌우로 연결된 노드를 묶어 묶음의 개수를 세는 방식.
```python
# 교재 풀이
n, m = map(int, input().split())
graph = [[0] for _ in range(n)]

for i in range(n):
    graph[i] = (list(map(int, input().split())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
```

## [문제] 미로 탈출
> 동빈이는 N * M 크기의 직사각형 형태의 미로에 갇혀 있다.
> 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다.
> 동빈이의 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다.
> 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다.
> 반드시 탈출할 수 있는 형태로 제시되며, 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.
> 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

-> bfs를 이용해 가까운 노드부터 차례대로 모든 노드를 탐색하는 방식.
```python
# 교재 풀이
from collections import deque

n, m = map(int, input().split())

graph = [[0] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]

result = bfs(0, 0)
print(result)
```
