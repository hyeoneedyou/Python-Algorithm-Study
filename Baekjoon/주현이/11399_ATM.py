n = int(input())
t = list(map(int, input().split()))
result = sorted(t)
res = 0
for i in range(n):
    res += result[i] * (n - i)
print(res)