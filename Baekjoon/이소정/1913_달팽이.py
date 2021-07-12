N = int(input())

board = [[0] * N for i in range(N)]
data = N*N # 9

# 모서리에 도달할 때마다 방향을 바꿔주면 됨
# 25부터 거꾸로 구현

for i in range(N) : # 열 같음
  for j in range(N) : # 행 달라짐
    board[j][i] = data
    data = data - 1
    if (j == N-1) :
      for i in range(N) :
        data = data -1
        board[j][i] = data
print(board)

#     i=0 i=1 i=2 i=3 i=4
# j=0  25
# j=1  24
# j=2  23
# j=3  22              16
# j=4  21  20  19  18  17

#     i=0 i=1 i=2
# j=0  9
# j=1  8
# j=2  7
