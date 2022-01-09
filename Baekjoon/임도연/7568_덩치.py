n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]


def count_bigger(base):
    cnt = 1
    for person in xy:
        if base[0] < person[0] and base[1] < person[1]:
            cnt += 1
    return cnt


for i in range(n):
    print(count_bigger(xy[i]), end=" ")
