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

print(first, second)

# 숫자를 더하자
m_count = 0
sum = 0
while(m_count<M) : # M번이 아직 더해지지 않았을 경우
  if (M<=K) :
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
