N = int(input())
d = [0] * (N + 1)
d[0], d[1], d[2] = 0, 1, 3

for i in range(3, N + 1):
  d[i] = (d[i - 1] + 2 * d[i - 2])
print(d[N] % 796796)