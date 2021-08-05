n = int(input())
d = [50001] * (n+1)
d[0] = 0

for i in range(n):
    for j in range(i**2, (n**2)+1):
        if d[j] != 50001:
            d[j] = min(d[j], d[j-n**2]+1)

if d[n] == 50001:
    print(-1)
else:
    print(d[n])