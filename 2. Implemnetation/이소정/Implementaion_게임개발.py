N, M = input().split() # N : 세로(행), M : 가로(열)
A, B, d = input().split() # (A, B)
N = int(N)
M = int(M)
A = int(A)
B = int(B)
d = int(d)

board = [[0] * M for i in range(N)] # N(행) X M(열) 보드판 생성 -> 0으로 초기화

board[A][B] = 1 # 현재 좌표 -> 1
earth = [] # 맵 정보, 육지 or 바다

for i in range(N) :
  new_list = list(map(int, input().split()))
  earth.append(new_list)

# 방향 -> 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
  global d
  if d == 0 :
    d = 3
  else :
    d -= 1

count = 1 # 처음 위치 방문
turn_time = 0

while True:
  turn_left() # 회전 북 -> 서(3)
  # 이동 예정인 칸
  x = A + dx[d]
  y = B + dy[d]
  if (earth[x][y] == 0 and board[x][y] == 0) :
    board[x][y] = 1
    A = x
    B = y
    count += 1
    turn_time = 0
    continue
  else : 
    turn_time += 1
  
  # 4방향 모두 갈 수 없다면
  if turn_time == 4 :
    # 한 칸 뒤로
    x = A - dx[d]
    y = B - dy[d]
    if earth[x][y] == 0 : # 육지
      A = x
      B = y
    else : # 바다
      break
    turn_time = 0

print(count)