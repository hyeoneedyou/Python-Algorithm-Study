# a, b의 최소 공배수 구하기

# 방법1. gcd 이용하기

import math

n = int(input()) # 테스트 케이스 개수
for _ in range(n):
  a, b = map(int, input().split())
  # 최소 공배수 * 최대 공약수 = a * b
  lcm = a * b / math.gcd(a, b)
  print(int(lcm))

# 방법2. lcm 직접 구현하기
# a = 4 | 4  8      24
# b = 6 | 6  6  12  6   12   24

# n = int(input())
# for _ in range(n):
#   a, b = map(int, input().split())
#   i = 1
#   j = 1

#   while True: # a
#     while True: # b
#       if a * i <= b * j:
#         break
#       else:
#         j += 1
#     if a * i == b * j:
#       print(a*i)
#       break
#     else:
#       i += 1
