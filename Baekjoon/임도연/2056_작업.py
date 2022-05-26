# 작업 : 1    2    3    4    5    6    7
# 시간 : 5    1    3    6    1    8    4
# 선행 : x    1    2    1    2,4  2,4  3,5,6
# 순서 : 1(5)
#       1    2(5 + 1)
#       1    2    3(5 + 1 + 3)
#       1    2    3    2(5 + 6)
#       1    2    3    2    4(5 + 6 + 1)
#       1    2    3    2    4   4(5 + 6 + 8)
#       1    2    3    2    4    4    5(5 + 6 + 8 + 4)

n = int(input())

work_time = [0 for _ in range(n + 1)]  # 작업 순서대로 시간 저장


def find_max_time_relation_work(relations):
    max_time = 0
    max_time_work = 0
    for w in relations:
        if max_time < work_time[w]:
            max_time = work_time[w]
            max_time_work = w

    return max_time_work


for i in range(1, n + 1):
    work = list(map(int, input().split()))
    time = work[0]
    relation_count = work[1]
    relation_works = work[2:]

    # 선행 업무중에서 가장 오래 걸리는 작업 찾기
    longest_work = find_max_time_relation_work(relation_works)
    work_time[i] = work_time[longest_work] + time

print(max(work_time))
