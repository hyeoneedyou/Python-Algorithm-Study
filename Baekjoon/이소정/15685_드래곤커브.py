# 0
# 01 -> 0 -> 1
# 0121 -> 10 -> 21
# 01212321 -> 1210 -> 2321
# 0121232123032321 -> 



n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1] # 0 1 2 3

arr = [[0] * 101 for _ in range(101)]

for _ in range(n):
  x, y, d, g = map(int, input().split())
  arr[x][y] = 1

  gen = [d]
  for _ in range(g): # 세대
    tmp = []
    for i in range(len(gen)):
      tmp.append((gen[-i-1] + 1) % 4)
    gen.append(tmp)

  for i in gen:
    nx = x + dx[i]
    ny = y + dy[i]
    arr[nx][ny] = 1
    x = nx
    y = ny

result = 0
for i in range(100):
  for j in range(100):
    if arr[i][j] == 1 and arr[i+1][j] == 1 and arr[i][j+1] == 1 and arr[i+1][j+1] == 1:
      result += 1

print(result)