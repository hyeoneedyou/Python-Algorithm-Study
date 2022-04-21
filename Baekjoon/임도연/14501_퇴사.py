# 3  5  1  1  2  4  2
# 10 20 10 20 15 40 200

n = int(input())
program = [list(map(int, input().split())) for _ in range(n)]
program.insert(0, [0, 0])

money = [0 for _ in range(n + 2)]
money[n] = 0 if program[n][0] > 1 else program[n][1]

for i in range(n - 1, 0, -1):
    if program[i][0] + i - 1 > n:  # 오늘 상담이 불가능한 경우
        money[i] = money[i + 1]
    else:  # 오늘 상담이 가능한 경우
        money[i] = max(program[i][1] + money[i + program[i][0]], money[i + 1])

print(money[1])
