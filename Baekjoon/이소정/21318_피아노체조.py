# N개의 악보
# 난이도
# 1 <= x <= y <= N
# x~y까지 순서대로 연주
# 난이도 순서대로, y는 실수ㄴㄴ
# 쉬운거 -> 어려운거

# i 0 1 2 3 4 5 6  7 8(N-1) 9(N) 
# * 1 2 3 3 4 1 10 8 1
# 0 1 2 3 4 5 6 7  8 9
# 0 0 0 0 0 1 1 2  3 0

# 시간초과
# N = int(input())
# level = list(map(int, input().split()))
# Q = int(input())

# for _ in range(Q):
#   x, y = map(int, input().split())
#   mistake = [0] * (N+1)
#   for i in range(0, N-1): # index 7까지 확인
#     if level[i] > level[i+1]: # 실수
#       mistake[i+1] = mistake[i] + 1
#     else:
#       mistake[i+1] = mistake[i]
#   print(mistake[y-1] - mistake[x-1])


# 시간초과의 원인
# for문 안에 for문이 존재(불필요하다면 이 방식은 지양하자)
# 줄바꿈으로 input값을 여러 번 받을 때는 sys.stdin.readline()을 적극 활용하자

import sys

N = int(input())
level = list(map(int, input().split()))
Q = int(input())
mistake = [0] * (N+1)

for i in range(0, N-1): # index 7까지 확인
  if level[i] > level[i+1]: # 실수
    mistake[i+1] = mistake[i] + 1
  else:
    mistake[i+1] = mistake[i]

for _ in range(Q):
  x, y = map(int, sys.stdin.readline().split())
  print(mistake[y-1] - mistake[x-1])