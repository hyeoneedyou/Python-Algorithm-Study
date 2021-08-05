n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_t = sorted(a)
b_t = b
b_t = b_t.sort()

res = []
for i in range(n):
    for j in range(n):
        if b_t[i] == b[j]:
            res.append(j)
print(res)
for i in range(n):
    a[res[i]] = a_t[n-i-1]

ans = 0
for i in range(n):
    ans += a[i]*b[i]
print(ans)