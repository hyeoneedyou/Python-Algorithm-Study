# 루트 없는 트리가 주어진다.
# 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

# import sys
# sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent_node = [0] * (n + 1)


def dfs(graph, v):
    stack = [v]
    while stack:
        node = stack.pop()
        for i in graph[node]:
            parent_node[i] = node
            stack.append(i)
            graph[i].remove(node)


# def dfs(graph, v, visited):
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             parent_node[i] = v
#             dfs(graph, i, visited)


dfs(graph, 1)

for i in range(2, n + 1):
    print(parent_node[i])