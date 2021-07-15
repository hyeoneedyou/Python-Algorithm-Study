# 루트 없는 트리가 주어진다.
# 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)

parent_node = [0] * (n + 1)


def dfs(graph, v, visited):
    pass


array = [0] * (n + 1)
dfs(graph, 2, array)
for i in range(2, n + 1):
    print()
