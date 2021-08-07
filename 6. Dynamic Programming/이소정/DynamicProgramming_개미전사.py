N = int(input()) # 식량창고 개수 4
K = list(map(int, input().split())) 

# 앞서 계산된 결과를 지정하기 위한 DP 테이블 초기화
d = [0] * 100
# 0 0 0 0 0 0 ... 0 0 0
d[0] = K[0]
d[1] = max(K[0], K[1])

# Dynami Programming 진행(Bottom-up)

for i in range(2, N): # 2부터 N-1까지
  d[i] = max(d[i - 1], d[i - 2] + K[i])

print(d[N - 1]) # index는 0부터
