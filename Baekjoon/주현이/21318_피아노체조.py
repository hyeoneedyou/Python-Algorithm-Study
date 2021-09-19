import sys
n = int(input())
d = list(map(int, sys.stdin.readline().split()))
q = int(input())
f = []
dp = [0] * n
for i in range(1, n):
    if d[i-1] > d[i]:
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i-1]
for i in range(q):
    ans = 0
    a, b = map(int, input().split())
    ans = dp[b-1] - dp[a-1]
    f.append(ans)

for i in range(len(f)):
    print(f[i])