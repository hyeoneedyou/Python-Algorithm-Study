t = int(input())

for _ in range(t):
    n = int(input())
    temp_score = [list(map(int, input().split())) for _ in range(n)]
    temp_score.sort()
    base = temp_score[0][1]  # 서류 성적 1위의 면접 성적을 기준으로 함

    temp_result = 1
    for i in range(1, n):
        if base == 1:
            break
        if temp_score[i][1] < base:
            temp_result += 1
            base = temp_score[i][1]
    print(temp_result)
