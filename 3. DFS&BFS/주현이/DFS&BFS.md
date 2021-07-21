# DFS & BFS

## 자료구조 기초

### 탐색(search)
-  많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
- 그래프, 트리 등의 자료구조 안에서 탐색하는 문제를 자주 다룸

### 자료구조(Data Structure)
- 데이터를 표현하고 관리하고 처리하기 위한 구조
- `스택`과 `큐`는 자료구조의 기초 개념이며 다음 두 핵심적인 함수로 구성됨
    - `삽입(Push)`: 데이터를 삽입한다.
    - `삭제(Pop)`: 데이터를 삭제한다.

#### 스택(Stack)
- 선입후출(FIFO)
- 파이썬에서 스택을 이용할 때에는 별도의 라이브러리를 사용할 필요가 없이 기본 리스트에서 `append()`와 `pop()`메서드를 이용하면 스택 자료구조와 동일하게 동작한다.
- 스택 예제

```python
stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)  # 최하단 원소부터 출력
print(stack[::-1])  # 최상단 원소부터 출력
```
#### 큐(Queue)
- 선입선출(FIFO)
- 파이썬으로 큐를 구현할 떄는 collections 모듈에서 제공하는 deque 자료구조를 활용하면 좋음
- deque는 스택과 큐의 장점을 모두 채택한 것으로, 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이며 queue 라이브러리를 이용하는 것보다 더 간단하다.
- 큐 예제
```python
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)  # 먼저 들어온 순서대로 출력
queue.reverse()  # 다음 출력을 위해 역순으로 바꾸기
print(queue)  # 나중에 들어온 원소부터 출력

# list(queue)를 하면 deque객체를 리스트 자료형으로 변경할 수 있다.
```

#### 재귀함수(Recursive Function)
- 자기 자신을 다시 호출하는 함수
- 재귀 함수 예제
```python
def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()
```
- 재귀 함수의 종료 조건을 명시하지 않으면 함수가 무한 호출될 수 있음
- 재귀 함수 초반에 등장하는 if문이 종료 조건 역할을 수행함
- 재귀 함수 종료 예제
```python
def recursive_functions(i):
    # 100번쨰 출력했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')

recrusive_functioni(1)
```
- 재귀 함수는 스택 자료구조와 동일. 따라서 스택 자료구조를활용해야 하느 ㄴ상당수 알고리즘은 재귀 함수를 이용해서 간편하게 구현될 수 있음. DFS가 대표적인 예임
- 두가지 방식으로 구현한 팩토리얼 예제
```python
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:
        return 1
    # n! = n * (n - 1)!을 그대로 코드로 작성하기
    return n * factorial_recursive(n - 1)

# 각각의 방식으로 구현한 n! 출력(n = 5)
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))
```

## 탐색 알고리즘 DFS/BFS
### DFS(Depth-First Search)
- 깊이 우선 탐색. 그래프에서 깊은 부분을 우선적으로 탐새하는 알고리즘
- 그래프: `노드(Node)`(또는 `정점(Vertex)`)와 `간선(Edge)`로 표현
- 그래프 탐색: 하나의 노드를 시작으로 다수의 노드를 방문하는 것
- 두 노드가 간선으로 연결되어 있다면 '두 노드는 인접하다(Adjacent)' 라고 표현
####  인접 행렬(Adjacency matrix)
- 2차원 배열로 그래프의 연결 관계를 표현
- 2차원 배열에 각 노드가 연결된 형태를 기록
- 파이썬 2차원 리스트로 구현
- `무한(Infinity)의 비용`: 연결이 되어 있지 않은 노드끼리
- 정답이 될 수 없는 큰 값(e.g. `999999999`, `987654321`)으로 데이터를 초기화
- 인접 행렬 방식 예제
```python
INF = 999999999 # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)
```
#### 인접 리스트(Adjacency List)
- 리스트로 그래프의 연결 관계를 표현
- 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장
- 파이썬 2차원 리스트로 구현
```python
# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장 (노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장 (노드, 거리)
graph[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장 (노드, 거리)
graph[2].append((0, 5))

print(graph)
```

#### `인접 행렬(Adjacency matrix)`과 `인접 리스트(Adjacency List)`의 차이점
1. 메모리 효율: `인접 행렬` < `인접 리스트`
- 인접 행렬 방식은 모든 관계를 저장하므로 노드 개수가 많을 수록 메모리가 불필요하게 낭비됨
2. 접근 속도: `인접 행렬` > `인접 리스트`
- 인접 리스트 방식에서는 연결된 데이터를 하나씩 확인해야 하기 때문에 정보를 얻는 속도가 느림

#### DFS 동작 과정
- 특정한 경로로 탐색하다가 특정한 상황에서 최대한 깊숙이 들어가서 노드를 방문한 후, 다시 돌아가 다른 경로롤 탐색
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 잇으면 그 인접 노드를 스택에 넣고 방문 처리. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복

    💡 `방문 처리`: 스택에 한 번 삽입되어 처리된 노드가 다시 삽입되지 않게 체크하는 것. 방문 처리를 함으로써 각 노드를 한 번씩만 처리할 수 있다.

- 인접한 노드 중에서 방문하지 않은 노드가 여러 개 잇으면 번호가 낮은 순서부터 처리
- 스택을 사용하지 않고 재귀 함수를 이용했을 때 간격하게 구현 가능
- O(N)
- DFS 예제
```python
# DFS 함수 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [], # 노드의 번호가 1번부터 시작하는 경우가 많으므로 비우둠
  [2, 3, 8], # 1번 노드는 2, 3, 8 노드와 연결됨
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
```

### BFS(Breath First Search)
- 너비 우선 탐색. 가까운 노드부터 탐색하는 알고리즘
- 큐 자료구조 이용(deque 라이브러리)
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복
- O(N) (일반적인 경우 실제 수행 시간은 DFS보다 좋은 편)
- BFS 예제
```python
from collections import deque

# BFS 함수 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
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

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
```

- 그래프 형태로 바꿔서 생각하면 좋음