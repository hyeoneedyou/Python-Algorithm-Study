# 어떠한 수 N이 1이 될 때까지 두 과정 중 하나를 반복적으로 선택하여 수행하려한다.
# 단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.
# N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하여라.

n, k = map(int, input().split())

cnt = 0
while n != 1:
    if n % k != 0:
        n -= 1
    else:
        n //= k
    cnt += 1

print(cnt)


# n, k = map(int, input().split())
#
# result = 0
# while True:
#     target = (n // k) * k
#     result += n - target  # 1번
#     n = target
#
#     if n < k:
#         break
#     result += 1
#     n //= k  # 2번
#
# result += (n - 1)
#
# print(result)
