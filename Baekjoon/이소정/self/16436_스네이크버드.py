# i 
# hi 
# 자신보다 작거나 같은 높이
# 처음 길이 L

N, L = map(int, input().split()) # 3 10
height = list(map(int, input().split()))
height.sort()

for i in range(N):
  if height[i] <= L:
    L += 1

print(L)