n, m = map(int, input().split())
money = [int(input()) for _ in range(n)]

left = min(money)
right = sum(money)


def calculate(base):
    remain = base
    withdraw_count = 1
    for cost in money:
        if remain < cost:
            remain = base
            withdraw_count += 1
        remain -= cost
    return withdraw_count


result = max(money)
while left <= right:
    mid = (left + right) // 2
    cal = calculate(mid)
    if cal > m or mid < max(money):
        left = mid + 1
    else:
        right = mid - 1
        result = mid

print(result)