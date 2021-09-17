T = int(input())

for _ in range(1, T+1):
  J, N = map(int, input().split())
  box = []
  for _ in range(1, N+1):
    R, C = map(int, input().split())
    box.append(R*C)
  box.sort(reverse=True)
  sum = 0
  for i in range(0, len(box)):
    sum += box[i]
    if sum >= J:
      print(i+1)
      break;

# 함수로 작성하는 것 보다는 바로 작성하는 것이 시간이 더 적게걸림
# T = int(input())

# def candyIn(box, J):
#   box.sort(reverse=True)
#   sum = 0
#   for i in range(0, len(box)):
#     sum += box[i]
#     if sum >= J:
#       return i+1

# for _ in range(1, T+1):
#   J, N = map(int, input().split())
#   box = []
#   for _ in range(1, N+1):
#     R, C = map(int, input().split())
#     box.append(R*C)
#   print(candyIn(box, J))

# 다른 방법
# import sys
# input = sys.stdin.readline

# t = int(input())

# for _ in range(t):
#     candy, box = map(int,input().split())
#     box_list = []
#     cnt=0
#     for i in range(box):
#         r,c = map(int,input().split())
#         box_list.insert(i,r*c)
    
#     box_list.sort(reverse=True)
#     for j in range(box):
#         candy = candy-box_list[j]
#         cnt += 1
#         if candy <=0:
#             break
#     print(cnt)