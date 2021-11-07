n = int(input())
p = list(map(int, input().split()))
p.sort()  # 오름차순 정렬이니까 항상 최소한의 모험가의 수만 포함하여 그룹 결성 -> 최대 그룹수

res = 0  # 그룹 수
cnt = 0  # 현재 그룹에 포함된 모험가의 수

for i in p:
    cnt += 1
    if cnt >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성 종료
        res += 1
        cnt = 0

print(res)

