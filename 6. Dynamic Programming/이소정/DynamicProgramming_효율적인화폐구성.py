# 0 -> 0
# 1 -> -1
# 2 = 2*1 -> 1
# 3 = 2*1 + d[1] -> -1
# 4 = 2*2 -> 2
# 5 = 5*1 -> 1
# 6 = 5*1 + 1
#   = 2*3 -> 3

N, M = map(int, input().split())
# N가지 화폐
# M원
a = []
for i in range(1, N + 1): # 1부터 M까지 입력 받기
  a.append(int(input()))

d = [10001] * (M + 1)
d[0] = 0
for i in range(1, M+1): # M원까지 
  for j in a:
    if i % j == 0:
      d[i] = i // j # 몫 넣기
    d[i] = min(d[i], (i // j) + d[i % j])

if d[M] == 10001:
  print(-1)
else: 
  print(d[M])