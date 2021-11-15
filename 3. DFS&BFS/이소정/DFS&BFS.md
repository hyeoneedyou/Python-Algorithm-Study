# 꼭 필요한 자료구조 기초

- `탐색(Search`)이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
- 프로그래밍에서는 그래프, 트리 등의 자료구조 안에서 탐색을 하는 문제를 자주 다룸
- 대표적인 탐색 알고리즘으로 DFS와 BFS를 꼽을 수 있는데, 이 두 알고리즘의 원리를 제대로 이해해야 함 -> 스택과 뷰에 대한 이해가 전제되어야 함
- `자료구조(Data Structure)`란 데이터를 표현하고 관리하고 처리하기 위한 구조
- 삽입(Push) : 데이터를 삽입
- 삭제(Pop) : 데이터를 삭제
- 오버플로(Overflow) : 특정한 자료구조가 수용할 수 있는 데이터의 크기를 이미 가득 찬 상태에서 삽입 연산을 수행할 때 발생. 즉, 저장 공간을 벗어나 데이터가 넘쳐흐를 때 발생
- 언더플로(Underflow) : 특정한 자료구조에 데이터가 전혀 들어 있지 않은 상태에서 삭제 연산을 수행하면 데이터가 전혀 없는 상태이므로 언더플로가 발생

<br>

## 스택

- 선입후출(First In Last Out)구조 또는 후입선출(Last In First Out)
- 아래에 있는 박스를 치우기 위해서는 위에 있는 박스를 먼저 내려야 함
- ```
  stack = []

  stack.append(5)
  stack.append(2)
  stack.append(3)
  stack.append(7)
  stack.pop()
  stack.append(1)
  stack.append(4)
  stack.pop()

  print(stack) # 최하단 원소부터 출력 # [5, 2, 3, 1]
  print(stack[::-1]) # 최상단 원소부터 출력 [1, 3, 2, 5]
  ```

<br>

## 큐

- 선입선출(First In First Out)구조
- 먼저 온 사람이 먼저 들어감
- ```
  from collections import deque

  # 큐(Queue) 구현을 위해 deque 라이브러리 사용
  queue = deque()

  queue.append(5)
  queue.append(2)
  queue.append(3)
  queue.append(7)
  queue.popleft()
  queue.append(1)
  queue.append(4)
  queue.popeleft()

  print(queue) # 먼저 들어온 순서대로 출력 dequeue([3, 7, 1, 4])
  queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
  print(queue) # 나중에 들어온 원소부터 출력 dequeue([4, 1, 7, 3])
  ```

- 파이썬으로 큐를 구현할 때는 collections 모듈에서 제공하는 dequeue 자료구조를 활용
- dequeue는 스택과 큐의 장점을 모두 채택한 것인데 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이며 queue 라이브러리를 이용하는 것보다 더 간단함
- 코딩테스트에서 collections 모듈과 같은 기본 라이브러리 사용을 허용
- dequeue 객체를 리스트 자료형으로 변경하고자 한다면 list() 메서드를 이용하면 됨. list(queue)를 하면 리스트 자료형으로 반환됨

<br>

## 재귀 함수

- 재귀 함수(Recursive Function)란 자기 자신을 다시 호출하는 함수
- ```
  def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

  recursive_function( )
  ```

- 수학 시간에 한 번씩 언급되는 프랙털(Practal)구조와 흡사함

<br>

### 재귀 함수의 종료 조건

- 재귀 함수를 무제 풀이에서 사용할 때는 재귀 함수가 언제 끝날지, 종료 조건을 꼭 명시해야 함. 자칫 종료 조건을 명시하지 않으면 함수가 무한 호출될 수 있음
- ```
  def recursive_function(i):
    if i == 100:
      return
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')

  recursive_function(1)
  ```

- 컴퓨터 내부에서 재귀 함수의 수행은 스택 자료구조를 이용함. 함수를 계속 호출했을 때 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료되기 때문임
- 스택 자료구조를 활용해야 하는 상당수 알고리즘은 재귀 함수를 이용해서 간편하게 구현될 수 있음. DFS가 대표적인 예

- ```
  def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
      result *= i
    return result

  print('반복적으로 구현:', factorial_iterative(5)) # 120

  def factorial_recursive(n):
    if n<=1:
      return 1
    return n * factorial_recursive(n-1)

  print('재귀적으로 구현:', factorial_recursive(5)) # 120
  ```

- 재귀 함수가 수학의 점화식을 그대로 소스코드로 옮겼기 때문에 재귀 함수의 코드가 더 간결함
- n이 1이하인 경우에는 1이 반환될 수 있도록 종료 조건을 구현함

<br>

# 탐색 알고리즘 DFS/BFS

## DFS

- Depth-First Search, 깊이 우선 탐색이라고 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
- 그래프는 노드(Node)와 간선(Edge)으로 표현되며 이때 노드를 정점(Vertex)이라고도 함
- 그래프 탐색이란 하나의 노드를 시작으로 다수의 노드를 방문하는 것을 말함
- 두 노드가 간선으로 연결되어 있다면 '두 노드는 인접하다(Adjacent)라고 표현

<br>

### 인접 행렬(Adjacency Matrix)

- 2차원 배열로 그래프의 연결 관계를 표현하는 방식
- 연결이 되어 있지 않은 노드끼리는 무한(Infinity)의 비용이라고 작성함. 실제 코드에서는 논리적으로 정답이 될 수 없는 큰 값 중에서 999999999, 987654321 등의 값으로 초기화함
- ```
  INF = 999999999 # 무한의 비용 선언

  # 2차원 리스트를 이용해 인접 행렬 표현
  graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
  ]

  print(graph)
  ```

<br>

### 인접 리스트(Adjacency List)

- 리스트로 그래프의 연결 관계를 표현하는 방식
- '연결 리스트'라는 자료구조를 이용해 구현하는데, C++나 자바와 같은 프로그래밍 언어에서는 별도로 연결 리스트 기능을 위한 표준 라이브러리를 제공하지만, 파이썬은 기본 자료형인 리스트 자료형이 append() 메소드를 제공함
- 파이썬으로 인접 리스트를 이용해 그래프를 표현하고자 할 때에는 단순히 2차원 리스트를 이용하면 됨
- ```
  # 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
  graph = [[] for _ in range(3 )]

  # 노드 0에 연결된 노드 정보 저장(노드, 거리)
  graph[0].append((1, 7))
  graph[0].append((2, 5))

  # 노드 1에 연결된 노드 정보 저장(노드, 거리)
  graph[1].append((0. 7))

  # 노드 2에 연결된 노드 정보 저장(노드, 거리)
  graph[2].append((0, 5))

  print(graph)
  ```

<br>

### 이 두 가지은 어떤 차이가 있을까?

- 메모리 측면
  - 인접 행렬 방식은 모든 관계를 저장하므로 노드 개수가 많을수록 메모리에 불필요하게 낭비
  - 인접 리스트 방식은 연결된 정보만을 저장하기 때문에 메모리를 효율적으로 사용
- 속도 측면
  - 위의 인접 리스트 방식의 특성때문에 인접 행렬 방식에 비해 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느림. 인접 리스트 방식에서는 연결된 데이터를 하나씩 확인해야 하기 때문임

<br>

### DFS 동작

1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 함
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 함(여러 개 있을 경우, 이 중에서 가장 작은 노드를 선택함). 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복함

- DFS는 스택 자료구조에 기초한다는 점에서 구현이 간단함
- 실제로는 스택을 쓰지 않아도 되며 탐색을 수행함에 있어서 데이터의 개수가 N개인 경우 O(N)의 시간이 소요됨
- DFS는 스택을 이용하는 알고리즘이기 때문에 실제 구현은 재귀 함수를 이용했을 때 매우 간결하게 구현할 수 있음
- ```
  def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ') # 1 2 7 6 8 3 4 5
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
      if not visited[i]:
        dfs(graph, i, visited)

  graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 7],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
  ]

  visited = [False] * 9

  dfs(graph, 1, visited)
  ```

<br>

## BFS

- Breath First Search, 너비 우선 탐색
- 가까운 노드부터 탐색하는 알고리즘
- 선입선출 방식인 큐 자료구조를 이용하는 것이 정석
- 인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성하면 자연스럽게 먼저 들어온 것이 먼저 나가게 되어, 가까운 노드부터 탐색을 진행하게 됨

<br>

### BFS 동작

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 함
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리 함
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복

<br>

- 큐 자료구조에 기초한다는 점에서 구현이 간단함. 실제로 구현함에 있어 앞서 언급한 대로 dequeue 라이브러리를 사용하는 것이 좋으며 탐색을 수행함에 있어 O(N)의 시간이 소요됨
- 일반적인 경우 실제 수행 시간은 DFS보다 좋은 편임
- ```
  from collections import deque

  # BFS 메서드 정의
  def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 dequeue 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
      # 큐에서 하나의 원소를 뽑아 출력
      v = queue.popleft()
      print(v, end=" ") # 1 2 3 8 7 4 5 6
      # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
      for i in graph[v]:
        if not visited[i]:
          queue.append(i)
          visited[i] = True

  graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 7],
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

<br>

## DFS vs BFS

|           | DFS            | BFS              |
| --------- | -------------- | ---------------- |
| 동작 원리 | 스택           | 큐               |
| 구현 방법 | 재귀 함수 이용 | 큐 자료구조 이용 |

```

```
