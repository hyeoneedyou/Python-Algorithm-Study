import math

s = input()
t = input()

# 이건 왜 안되지?
# if s in t or t in s:
#   print(1)
# else :
#   print(0)

len_s = len(s)
len_t = len(t)

lcm = int((len_s * len_t) / math.gcd(len_s, len_t)) # gcd * lcm = len_s * len_t -> 필요없는 코드

if s * int((lcm / len_s)) == t * int((lcm / len_t)) : # lcm / len_s = len_t / gcd -> lcm 정의 필요 없이 gcd만 가지고 풀이 가능
  print(1)
else :
  print(0)

# 위에를 짧게 쓰면 아래와 같다.
# import math
# a, b = input(), input()
# g = math.gcd(len(a), len(b))
# print(1 if a * (len(b) // g) == b * (len(a) // g) else 0)


# 굳이 최소공배수를 안하고 시간 조금 더 걸리더라도 간단하게 풀자.
# s = str(input())
# t = str(input())

# if s * len(t) == t * len(s):
#   print(1)
# else:
#   print(0)