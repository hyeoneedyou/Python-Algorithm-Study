N, M = map(int, input().split())
H = list(map(int, input().split()))

# high = max(H)
# low = 1

# while(low <= high) :
#   mid = (low + high) // 2
#   count = 0
#   for i in H :
#     if (i in H) :
#       if (i - mid > 0) :
#         count += (i - mid)
#   if count >= M : # 적어도 손님이 원하는 양 이상으로 준비
#     low = mid + 1
#   else :
#     high = mid - 1

# print(high) # high 값을 return해야 함

# 재귀함수
def cooking(target, list, start, end) :
  mid = (start + end) // 2
  count = 0
  if (start > end) :
    return end
  for i in H :
    if (i in H) :
      if (i - mid > 0) :
        count += (i - mid)
  if count >= M :
    return cooking(target, list, mid+1, end)
  else :
    return cooking(target, list, start, mid-1)

print(cooking(M, H, 0, max(H)))