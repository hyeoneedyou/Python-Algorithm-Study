# 0 0 0 0 0 0 0 

# 물을 한 번주면 무조건 3 증가
# 3으로 나눈 몫이 물을 준 횟수
# 1 1 1 3

# 1 2 1 5 
# -> 몫 : 0 1 0 2
# -> 나머지 : 1 0 1 1

# 1 3 1 3 1
# -> 몫 : 0 1 0 1 0
# -> 나머지 : 1 1 1 1 1

# 4 5
# -> 몫 : 2 2
# -> 나머지 : 0 1

# 10000 1000 100
# -> 몫 : 5000 500 50
# -> 나머지 : 0 0 0

# 2 4 6
# -> 몫 : 1 2 3 (물뿌리개 2)
# -> 나머지 : 0 0 0

# -> 몫 : 1 1 2
# -> 나머지 : 0 2 2
# 몫 - x = 나머지 + 2x
# 몫 - 나머지 = 3x

N = int(input())
height = list(map(int, input().split()))

remainder = 0 # 나머지
quo = 0 # 몫

for i in height:
  quo += i // 2
  remainder += i % 2

if (quo - remainder) % 3 == 0 and quo >= remainder:
  print("YES")
else :
  print("NO")
