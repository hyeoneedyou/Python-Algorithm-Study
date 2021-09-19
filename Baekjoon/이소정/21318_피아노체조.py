# N개의 악보
# 난이도
# 1 <= x <= y <= N
# x~y까지 순서대로 연주
# 난이도 순서대로, y는 실수ㄴㄴ
# 쉬운거 -> 어려운거
# 3 2
# X O

# i 0 1 2 3 4 5 6  7 8(N-1) 9(N) 
# * 1 2 3 3 4 1 10 8 1
# 0 1 2 3 4 5 6 7  8 9
# 0 0 0 0 0 1 1 2  3 0

# 시간초과
N = int(input())
level = list(map(int, input().split()))
Q = int(input())

for _ in range(Q):
  x, y = map(int, input().split())
  mistake = [0] * (N+1)
  for i in range(0, N-1): # index 7까지 확인
    if level[i] > level[i+1]: # 실수
      mistake[i+1] = mistake[i] + 1
    else:
      mistake[i+1] = mistake[i]
  print(mistake[y-1] - mistake[x-1])