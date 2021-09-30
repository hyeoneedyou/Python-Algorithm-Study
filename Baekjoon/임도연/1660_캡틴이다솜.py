n = int(input())
tri = []
data, temp, total = 1, 2, 1

while True:
    if total > n:
        break
    tri.append(total)
    data += temp
    temp += 1
    total += data

dp = [300001] * (n + 1)
for i in tri:
    dp[i] = 1
dp[0] = 0

for i in range(len(tri)):
    for j in range(tri[i], n + 1):
        dp[j] = min(dp[j], dp[j - tri[i]] + 1)

print(dp[n])