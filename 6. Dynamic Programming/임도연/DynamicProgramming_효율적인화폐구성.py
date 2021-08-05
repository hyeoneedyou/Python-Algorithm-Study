# n가지 종류의 화폐들의 개수를 최소한으로 이용해 그 가치의 합이 m원이 되도록 한다.
# 각 화폐는 개수 제한이 없으며, 사용 화폐 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.

n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0

for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])