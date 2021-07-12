# 배열의 크기, 숫자가 더해지는 횟수, 연속해서 더할 수 있는 횟수
N, M, K= input().split() 
N = int(N)
M = int(M)
K = int(K)

num = list(map(int, input().split()))

# 가장 큰 두 개의 수 반환
num.sort()
first = num[-1]
second = num[-2]

# 숫자를 더하자
m_count = 0
sum = 0
while(m_count<M) : # M번이 아직 더해지지 않았을 경우
  if (M<=K) : # 애초에 문제에서 K는 M보다 작거나 같다고 하였으므로 데드코드
    sum = first * M
    m_count += M # 거짓이므로 while문을 벗어남
  else : # M>K
    k_count = 0
    while(True) :
      k_count += 1
      m_count += 1
      sum += first
      if (k_count == K or m_count == M) :
      # K번이 더해지거나 M번을 더했을 경우 -> 멈춰야 함
        break;
    if (m_count == M) :
      break;
    if (k_count == K) :
      sum += second
      m_count += 1

print(sum)

# solution

# n,m, k = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort()
# first = data[n-1]
# second = data[n-2]

# result = 0

# while True:
#   for i in range(k): # 가장 큰 수 K번 더하기
#     if m == 0: # m이 0이라면 반복문 탈출
#       break
#     result += first
#     m -= 1 # 더할 때마다 1씩 빼기
#   if m == 0:
#     break
#   result += second # 두 번째로 큰 수를 한 번 더하기 
#   m -= 1 # 더할 때마다 1씩 빼기

# print(result)
