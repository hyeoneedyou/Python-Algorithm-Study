# 개미전사가 일직선으로 이어진 여러 식량창고를 선택적으로 약탈
# 최소 한 칸 이상 떨어진 식량 창고를 약탈해야할 때, 획득 식량의 최댓값을 구하라.

n = int(input())
array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])