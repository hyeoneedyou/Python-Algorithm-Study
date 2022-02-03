# N일
# M번
# K원

# 1000원 인출
# 100 400 300 100 500 101 400
# 900 500 200 100
#                 500 399
#                         600
# 3번 인출 < 5번 -> 인출 금액 줄여야 함

n, m = map(int, input().split())
prices = list(int(input()) for _ in range(n))

left = min(prices)
right = sum(prices)

def binary():
    cash = mid
    cnt = 1
    for price in prices:
        if price > cash: # 부족함
            cnt += 1
            cash = mid # 충전
        cash -= price
    return cnt

while(left <= right):
    mid = (left + right) // 2
    cnt = binary()
    # 이게 문제...!!ㅠㅠㅠ
    if cnt > m or mid < max(prices): # 인출 금액이 작음 -> 키우자
        left = mid + 1
    else: # 인출 금액이 큼 -> 줄이자
        right = mid - 1

print(left)
