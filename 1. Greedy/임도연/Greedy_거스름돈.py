# 거스름돈으로 500, 100, 50, 10원짜리 동전이 무한히 존재한다고 한다.
# 거슬러 줘야 할 돈이 N원일 때, 거슬러 줘야 할 동전의 최소 개수를 구하라.
# 단, N은 항상 10의 배수이다.
n = int(input())

m = [500, 100, 50, 10]
cnt = 0

for i in m:
    if n == 0:
        break
    cnt += n // i
    n %= i

print(cnt)


# 교재 풀이
# n = 1260
# count = 0
#
# coins_types = [500, 100, 50, 10]
#
# for coin in coins_types:
#     count += n // coin
#     n %= coin
#
# print(count)
