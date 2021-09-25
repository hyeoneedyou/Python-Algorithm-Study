n, w = map(int, input().split())
coins = [int(input()) for _ in range(n)]

buy = 0
for i in range(n - 1):
    # 가격이 상승하고 현금이 여유있을 때 구매
    if coins[i] < coins[i + 1] and w // coins[i] > 0:
        buy = w // coins[i]
        w -= buy * coins[i]
    # 어제보다 가격이 떨어졌으면 판매
    elif coins[i] > coins[i + 1]:
        w += buy * coins[i]
        buy = 0

# 마지막 날에 다 팔기
if buy > 0:
    w += buy * coins[-1]
print(w)
