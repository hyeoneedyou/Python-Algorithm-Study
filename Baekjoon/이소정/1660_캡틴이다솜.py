# pypy 코드
# 1                     -> 0 + [1]        0
# 1 + 2 = 3             -> 1 + [2] = 4    1
# 1 + 2 + 3 = 6         -> 4 + [3] = 10   2
# i(i+1)/2              -> 10 + [4] = 20
#                        
# 1, 4, 10, 20... 등의 인덱스를 가지는 요소 : 1

N = int(input())
INF = 1e9
dp = [INF] * (N+1) # 0 1 0 0 1 0 0 0 0 0 1 0 0 0 0 0 -> 길이 : 16
dp[0], dp[1] = 0, 1
tri = [1] # 1 4 10 20 35 56 82 120 ......

index = 1
while tri[-1] < len(dp):
  tri.append(tri[index-1] + ((index+1)*(index+2)//2))
  index += 1
tri.pop()

for i in tri:
  dp[i] = 1

for i in range(2, N+1): # 8
  for j in tri: # 1 + 7, 4 + 4
    if j < i:
      dp[i] = min(dp[i], dp[j] + dp[i-j]) # dp[1] + dp[4]

print(dp[N])


# python 코드
# N = int(input())
# INF = 1e9
# dp = [INF] * (N+1)
# dp[0] = 0
# tri = [1] 

# i = 2
# while True:
#   value = tri[-1] + (i * (i + 1)) // 2
#   if value > 300000:
#     break
#   else:
#     tri.append(value)
#   i += 1

# for j in range(1, N + 1):
#   for v in tri:
#     if j - v < 0: # out of range
#       break
#     else: # 1 4 10
#       # dp[v] = 1
#       # dp[j] = min(dp[j], dp[v] + dp[j-v])
#       if dp[j - v] + 1 < dp[j]:
#         dp[j] = dp[j - v] + 1

# print(dp[N])