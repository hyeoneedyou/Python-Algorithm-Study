# T -> S
# 맨 뒤에 A 제거
# 맨 앞에 B제거 -> 뒤집기

S = input()
T = input()
answer = 0

def solution(str):
  global answer

  if answer == 1:
    return 1

  if str == S:
    return 1
  if len(str) <= len(S):
    return 0

  if str[-1] == 'A':
    answer = solution(str[:-1])

  if str[0] == 'B':
    temp = str[1:]
    answer = solution(temp[::-1])

  return answer
  
print(solution(T))

# 재귀는 어렵다...