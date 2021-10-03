# 1 켜져있음
# 0 꺼져있음
# 1 <=  <= 스위치 개수
# 남학생(1) : 스위치 번호가 자기가 받은 수의 배수 -> 스위치 상태 바꿈
# 여학생(2) : 자기가 방은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭, 가장 많은 스위치 포함


N = int(input()) # 스위치 개수
state = list(map(int, input().split())) # 스위치 상태
num = int(input()) # 학생 수
for _ in range(num):
  gender, card = list(map(int, input().split())) # 성별, 받은 수

  # 남학생일 경우
  if gender == 1:
    for j in range(1, N//card + 1):
      state[card*j-1] = not bool(state[card*j-1])
  else:
    state[card-1] = not bool(state[card-1]) # 자기자신
    for k in range(1,min(card-1,N-card)+1):
      if state[card-k-1] == state[card+k-1]: 
        state[card-k-1] = not bool(state[card-k-1])
        state[card+k-1] = not bool(state[card+k-1])
      else:
        break
  state = list(map(int, state))

count = 0
for i in range(len(state)):
  print(state[i], end=" ")
  count += 1
  if (count+1) % 20 == 1:
    print("")
