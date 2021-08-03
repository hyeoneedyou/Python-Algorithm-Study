N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_list.sort() # 정렬

# 이진 탐색
def binary_search(list, target, start, end) :
  if len(list) == 0 or start > end:
    return "no"
  mid = (start + end) // 2 # index
  if list[mid] < target :
    return binary_search(list, target, mid+1, end)
  elif list[mid] > target :
    return binary_search(list, target, start, mid-1)
  else :
    return "yes"

for i in M_list :
  print(binary_search(N_list, i, 0, len(N_list)-1), end=" ")


# 파이썬 내장 함수
# for i in M_list :
#   if i in N_list :
#     print("yes", end=" ")
#   else :
#     print("no", end=" ")
  

