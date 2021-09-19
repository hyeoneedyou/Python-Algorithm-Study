# N개의 길
# 가로등 M개
# 가로등의 위치 x
# 높이만큼 주위를 비출 수 있고, 높을 수록 가격이 비쌈
# 최소한의 높이로 모든 길을 밝히고자 함
# 최소한의 예산을 구하자
# 가로등의 높이는 모두 같아야 하고, 정수이다

# 높이 H -> 왼쪽으로 H, 오른쪽으로 H

import math

N = int(input()) # 굴다리의 길이
M = int(input()) # 가로등의 개수
x = list(map(int, input().split()))
# print("x는 : ", x)

# 0 0 0 0 0 N -> N+1개
position = [0] * (N+1)
check = sorted(list(set([0] + x + [N])))
gap = []

# print("check는 : ", check)

gap.append(check[1]-check[0])
for i in range(2, len(check)-1):
  gap.append(math.ceil((check[i] - check[i-1])/2))
gap.append(check[-1]-check[-2])
# print("gap은 : ", gap)

print(max(gap))