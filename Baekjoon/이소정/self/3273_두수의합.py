n = int(input())
arr = list(map(int, input().split()))
x = int(input())

# arr에 있는 요소 2개를 더해 x를 만들자

# 시간초과
# count = 0

# for i in arr:
#   find = x - i
#   if find in arr[arr.index(i):]:
#     count += 1

# print(count)

arr.sort()

left = 0
right = n-1
count = 0

while left < right:
  if arr[left] + arr[right] == x:
    count += 1
    left += 1
    right -= 1
  elif arr[left] + arr[right] > x:
    right -=1
  else :
    left += 1

print(count)