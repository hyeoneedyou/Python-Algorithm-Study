# 한 단원 한 문제

# n 단원 개수, t 공부 총 시간
n, t = map(int, input().split())

# 단원별 (공부시간, 배점)의 쌍
study = [list(map(int, input().split())) for _ in range(n)]
study.insert(0, [0, 0])

result = [[0 for _ in range(t + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, t + 1):
        time = study[i][0]
        score = study[i][1]
        if j >= time:
            result[i][j] = max(result[i - 1][j], result[i - 1][j - time] + score)
        else:
            result[i][j] = result[i - 1][j]

print(result[n][t])
