n = int(input())
# n_num = list(map(int, input().split())) 
n_num = set(map(int, input().split())) # set 사용해보자.

m = int(input())
m_num = list(map(int, input().split()))

for i in m_num :
  if i in n_num :
    print(1, end=" ")
  else :
    print(0, end=" ")