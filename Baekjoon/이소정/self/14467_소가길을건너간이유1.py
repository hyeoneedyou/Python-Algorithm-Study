# 1 2 3 4 5 6 7 8 9 10
# 1 0 0 0 1 1 1 1 0 1

N = int(input())
count = 0
position = [-1] * N
for _ in range(N) :
  a, b = map(int, input().split()) # 소 번호, 위치
  if position[a-1] != -1 and position[a-1] != b: # -1이 아닐 때, -1이 아니면서 이전 이랑 다를 때
    count += 1
  position[a-1] = b
  # print(position, count)

print(count)