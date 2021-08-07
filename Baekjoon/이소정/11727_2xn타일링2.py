n = int(input())
# d = [0] * (n + 1)
# d[0], d[1], d[2] = 0, 1, 3
d = [0, 1, 3]

for i in range(3, n + 1):
  d.append(d[i-1] + d[i-2] * 2)
print(d[n] % 10007)

# 이미 할당된 리스트가 더 효율적이다