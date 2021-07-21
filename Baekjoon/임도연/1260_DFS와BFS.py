# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
# 입력으로 주어지는 간선은 양방향이다.
from collections import deque

n, m, v = map(int, input().split())

array = [[0, 0] for _ in range(m)]
graph = [[]]

# 입력 값 받기
for i in range(m):
    array[i] = list(map(int, input().split()))


# 인접 리스트로 정렬
for i in range(n):
    graph.append([])
    for j in range(m):
        if (i + 1) in array[j]:
            graph[i + 1].append(array[j][0] if array[j][0] != (i + 1) else array[j][1])
    graph[i].sort()


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    visited[v] = True
    queue = deque([v])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

array1 = [False] * (n + 1)
dfs(graph, v, array1)
print()
array1 = [False] * (n + 1)
bfs(graph, v, array1)
