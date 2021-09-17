# 처음에 index[0]번째를 누르냐, 안누르냐가 중요

# -1을 포함하는 최솟값을 리턴하라는 문제는 -1을 임의로 1e9라고 두고 풀이. -> 더 좋은 받법이 있는지 확인

N = int(input())
origin_= list(map(int, input()))
want = list(map(int, input()))

origin1 = origin_.copy()
origin2 = origin_.copy()

# 0->1, 1->0 으로 변경
def change(i, origin):
  for j in range(i-1, i+2):
    if j >= N or j < 0 :
      continue
    else :
      if origin[j] == 0:
        origin[j] = 1
      else:
        origin[j] = 0
  return origin

# 같은지 확인
def judge(origin, count) :
  if origin == want:
    return count
  else : 
    return 1e9

# 0번째 누름
def zeroClick() :
  count1 = 1
  change(0, origin1)
  for i in range(0, N-1):
    if origin1[i] != want[i]:
      change(i+1, origin1) 
      count1 += 1
  return judge(origin1, count1)
  

# 0번째 안누름
def notZeroClick() :
  count2 = 0
  for i in range(0, N-1):
    if origin2[i] != want[i]:
      change(i+1, origin2) 
      count2 += 1
  return judge(origin2, count2)

result = min(zeroClick(), notZeroClick())
if result == 1e9:
  print(-1)
else :
  print(result)