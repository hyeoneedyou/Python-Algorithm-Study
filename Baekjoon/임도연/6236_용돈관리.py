n, m = map(int, input().split())
money = [int(input()) for _ in range(n)]

left = min(money)
right = sum(money)


def calculate(base):
    remain = 0
    withdraw_count = 0
    for cost in money:
        if remain < cost:
            temp = cost
            while temp > 0:
                temp -= base
                withdraw_count += 1
            remain = temp * (-1)
        else:
            remain -= cost
    return withdraw_count


while left <= right:
    mid = (left + right) // 2
    result = calculate(mid)
    if result <= m:
        right = mid - 1
    elif result > m or mid < max(money):
        left = mid + 1

print(left)