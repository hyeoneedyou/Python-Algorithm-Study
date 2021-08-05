import math
n = int(input())
d = [5] * (n+1)
d[1] = 1

for i in range(2, n + 1):
    if math.sqrt(i).is_integer():
        d[i] = 1
    for j in range(1, int(math.sqrt(i)) + 1):
        d[i] = min(d[i], d[i - j**2] + d[j**2])

print(d[n])
