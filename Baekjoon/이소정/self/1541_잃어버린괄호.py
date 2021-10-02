# 55 - (50 + 40) - 10
# -가 나올 때 괄호를 치고, -가 또 나올 때 괄호를 닫는다.

arr = input().split("-")
for i in range(len(arr)):
  result = 0
  sub = arr[i].split("+")
  for j in range(len(sub)):
    result += int(sub[j])
  arr[i] = result
print(2*arr[0]-sum(arr))