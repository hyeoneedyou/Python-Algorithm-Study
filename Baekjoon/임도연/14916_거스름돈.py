# 춘향이는 편의점 카운터에서 일한다.
# 손님이 2원짜리와 5원짜리로만 거스름돈을 달라고 한다.
# 2원짜리 동전과 5원짜리 동전은 무한정 많이 가지고 있다.
# 동전의 개수가 최소가 되도록 거슬러 주어야 한다.
# 거스름돈이 n인 경우, 최소 동전의 개수가 몇 개인지 알려주는 프로그램을 작성하시오.

n = int(input())
m = [5, 2]

mx = n // 5
my = n // 2

result = n
for x in range(mx, -1, -1):
    for y in range(my + 1):
        if 5 * x + 2 * y == n:
            result = min(result, x + y)

if result == n:
    result = -1
print(result)
