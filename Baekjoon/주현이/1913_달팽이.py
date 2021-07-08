n = int(input())
b = int(input())
a = [[1]*n for _ in range(n)]

number = n**2
cycle = n - 3
for j in range(0, cycle):
    for i in range(0+j, n-j):
        a[i][0+j] = number
        number -= 1

    for i in range(1+j, n-j):
        a[n-1-j][i] = number
        number -= 1

    for i in range(1+j, n-j):
        a[n-1-i][n-1-j] = number
        number -= 1

    for i in range(1+j, n-1-j):
        a[0+j][n-1-i] = number
        number -= 1

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()

for i in range(n):
    for j in range(n):
        if a[i][j] == b:
            x = i+1
            y = j+1
print(x, y)

# 런타임에러