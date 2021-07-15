# 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 컴퓨터는 웜 바이러스에 걸리게 된다.
# 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어
# 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다.
# 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.
# 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다.
# 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때,
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

n = int(input())  # 컴퓨터 수
m = int(input())  # 연결된 컴퓨터 쌍 수

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
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


array = [0] * (n + 1)
dfs(graph, 1, array)

print(array.count(1) - 1)