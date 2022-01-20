# [Y][X]
# N(행) X M(열)
# Y Y+1
# 1 1 * * * * * * * *  X
# * 1 * * * * * * * *  X+1
# * * * * 1 * * * * *  X+2
# * * * * 1 * * * * * 
# * * 1 1 * * * 1 1 1 
# * * * * 1 * * 1 1 1 
# * * * * * * * 1 1 1 
# * * * * * * * * * * 

# 가로 M(Y), 세로 N(X)
import sys
sys.setrecursionlimit(10**6)

def make_graph(M, N, K):
  graph = [[0] * M for _ in range(N)]
  for _ in range(K):
    X, Y = map(int, input().split())
    graph[Y][X] = 1
  return graph

def dfs(X, Y): # 행 열
  #     상 하 좌 우
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  if X<0 or X>=N or Y<0 or Y>=M:
    return False

  if  graph[X][Y] == 0:
    return False

  graph[X][Y] = 0
  for i in range(4):
    nx = X + dx[i]
    ny = Y + dy[i]
    dfs(nx, ny)

T = int(input())
for _ in range(T):
  M, N, K = map(int, input().split())
  graph = make_graph(M, N, K)
  cnt = 0
  for i in range(N):
    for j in range(M): 
      if graph[i][j] == 1: 
        cnt += 1
        dfs(i, j) 

  print(cnt)

