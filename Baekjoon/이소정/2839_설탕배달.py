N = int(input())
count = 0

while True:
  if (N % 5) == 0: # 5의 배수
    count += (N // 5)
    print(count) 
    break
  else : # 5의 배수가 아니면
    N -= 3 # 5의 배수가 될 때까지 3을 뺀다
    count += 1
  if N < 0:
    print("-1")
    break