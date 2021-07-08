N = int(input())

board = [[0] * N for i in range(N)]
data = N*N

# 모서리에 도달할 때마다 방향을 바꿔주면 됨
# 25부터 거꾸로 구현

for i in range(N) : # 열 같음
  for j in range(N) : # 행 달라짐
    data = data - 1
    board[j][i] = data
    print(data)

print(board)