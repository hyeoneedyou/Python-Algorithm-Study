N = int(input())
num = int(input())

board = [[0] * N for i in range(N)]
data = N*N # 9

# 현재 위치
A = 0
B = 0

# 현재 방향
dir = 2

# 북 0 동 1 남 2 서3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
  global dir
  if dir == 0:
    dir = 3
  else:
    dir = dir -1


go_count = 0
turn_count = 0
go_row = N-1
first_turn = 0
board[A][B] = data # 처음 위치 표시

while(True):
  A = A + dx[dir]
  B = B + dy[dir]
  go_count += 1
  data -= 1
  if (data == num):
    x = A + 1
    y = B + 1
  board[A][B] = data
  if (data == 1):
    break;
  if (go_count == go_row): # 2
    turn_left()
    turn_count += 1
    go_count = 0
  if (first_turn == 0 and turn_count == 3):
    go_row = go_row - 1
    turn_count = 0
    first_turn = 1
  if (first_turn == 1 and go_count == 0):
    if turn_count == 2:
      go_row = go_row -1
      turn_count = 0

for i in range(N):
  for j in range(N):
    print(board[i][j], end=' ')
  print()
print(x, y)