n = int(input())
d = [0] * (n + 1) # 0~4까지만 들어갈 수 있음
d[0], d[1] = 0, 1

for i in range(2, n+1):
  min_value = 1e9 # 최솟값을 찾는 것이기 때문에 임의의 큰 값을 넣어준다.
  j = 1

  while (j**2) <= i:
    # 예를 들어, 11339이라고 해보자. 
    # j = 105일 때, i - 105^2 = 314 -> i보다 작은 최대의 제곱수는 아니지만, d[314] = 2 가 더 작다.
    # j = 106일 때, i - 106^2 = 103 -> i보다 작은 최대의 제곱수이지만, d[103] = 4 이 더 크다.
    # 따라서 min 함수가 꼭 필요하다.
    
    min_value = min(min_value, d[i - (j**2)])
    j += 1

  d[i] = min_value + 1
print(d[n])