# n = int(input())
#
# dp = [0] * (n+1)
# prev = 0  # 이전 삼각형 대포알 수
# size = 1  # 더해져야할 대포알 수
# now = 0  # 대포알 개수
# total = 0  # 총 대포알 수
# cnt = 0  # 사면체 개수
#
# while True:
#     now = prev + size
#     total += now
#     dp[size] = total
#     size += 1
#     if total >= n:
#         break
#     prev = now
#
# while True:
#     if n < 0:
#         break
#
#     if n >= dp[size]:
#         n -= dp[size]
#         cnt += 1
#     else:
#         size -= 1
#
# print(cnt)


n = int(input())

coins = []
coin, temp, len_coin = 1, 2, 0
total = 1

while True:
    if total > n:
        break
    coins.append(total)
    coin += temp
    temp += 1
    total += coin

size = len(coins)
dp = [300001 for _ in range(n+1)]
for i in coins:
    dp[i] = 1
dp[0] = 0

for i in range(size):
    for j in range(coins[i], n+1):
        dp[j] = min(dp[j], dp[j - coins[i]] + 1)

print(dp[n])