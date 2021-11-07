t = int(input())


def p(x):
    ans = 0
    # 1 1 1 2 2 3 4 5 7 9
    c = [1, 1, 1, 2, 2]
    if x <= 5:
        return c[x-1]
    if x > 5:
        for i in range(5, x):
            c[i] = c[i-3] + c[i-2]
        return c[x-1]


for _ in range(t):
    x = int(input())
    print(p(x))
    