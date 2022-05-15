# o x x o x x o x x
# x x x x x x x x x
# x x x x x x x x x
# x x x x x x x x x
# x x x x x x x x x
# x x x x x x x x x
# x x x x x x x x x
# x x x x x x x x x
# x x x x x x x x x


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

minusOne = 0
zero = 0
plusOne = 0

# 시작 x, y, 한 변의 길이
def conquer(x, y, n):
  global minusOne, zero, plusOne

  num = matrix[x][y]
  for i in range(x, x+n):
    for j in range(y, y+n):
      if matrix[i][j] != num:
        # 종이 한 장을 9등분
        for k in range(3):
          for l in range(3):
            conquer(x+k*(n//3), y+l*(n//3), n//3)
        return
  # 모두 num이랑 같을 때
  if num == -1:
    minusOne += 1
  elif num == 0:
    zero += 1
  else:
    plusOne += 1

conquer(0, 0, N)
print(minusOne)
print(zero)
print(plusOne)
