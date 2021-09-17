# 11 -> 1011 : 1001 -> 1100
# 12 -> 1100

# 비트 우정지수 확인 함수
def woojung(N, M) :
  # 다른 것들 중 
  # 0의 개수, 1의 개수 중 작은 것 만큼 swap
  # 남은 것들은 0->1, 1-> 0

  length = len(N) # 총 자리수
  one, zero = 0, 0 # N기준 1의 개수, 0의 개수

  for i in range(length) :
    if N[i] != M[i] : # 다르면
      if N[i] == '0':
        zero += 1
      else : 
        one += 1
  # 최소 : min(zero, one) 만큼 swap + max(zero, one) - min(zero, one) = max(zero, one)
  return max(zero, one)

T = int(input())
for _ in range(1, T+1): # 1부터 T까지 -> T번 반복
  N, M = map(str, input().split())
  print(woojung(N, M))