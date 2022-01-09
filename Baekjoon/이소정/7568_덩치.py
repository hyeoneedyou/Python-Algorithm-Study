# 몸무게 순서대로 정렬

# 88 186 -> (1, 1)
# 60 175 -> (2, 2)
# 58 183 -> (2, 3)
# 55 185 -> (2, 4)
# 46 155 -> (5, 5)

N = int(input())
arr = []
for _ in range(N):
  arr.append(list(map(int, input().split())))

for i in arr: # 나
  count = 1
  for j in arr:
    if i[0] < j[0] and i[1] < j[1]: # 나보다 덩치 큰 사람 찾기
      count += 1

  print(count, end=" ")