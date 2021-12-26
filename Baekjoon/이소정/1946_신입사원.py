# 1 4 -> 합격
# 2 3 -> 4보다 높아야 함
# 3 2 -> 3보다 높아야 함
# 4 1 -> 2보다 높아야 함
# 5 5 -> 1보다 높아야 함

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  cnt = 1
  N = int(input())
  people = [list(map(int, input().split())) for _ in range(N)]
  people.sort()
  max = people[0][1] # 비교대상

  for i in range(1, N):
    if max == 1:
      break
    if people[i][1] < max:
      cnt += 1
      max = people[i][1]
  print(cnt)