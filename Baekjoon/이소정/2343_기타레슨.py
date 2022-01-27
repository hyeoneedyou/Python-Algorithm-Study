# 하나의 블루레이에 담는 크기 탐색
# 1 2 3 4 5 6 7 8 9

# 9(left) >>>>>>>>>> 45(right)
# 9 <27 : mid> 45
# 1 2 3 4 5 6 // 7 8 9 -> 2개 : 탈락
# 9 <17> 27-1 = 26
# 1 2 3 4 5 // 6 7 // 8 9 -> 3개
# 9 <12> 16
# 1 2 3 4 // 5 6 // 7 // 8 // 9 -> 5개
# 13 <15> 16
# 1 2 3 4 5 // 6 7 // 8 // 9 -> 4개

n, m= map(int, input().split())
length = list(map(int, input().split()))

right = sum(length) # 45
left = max(length) # 9

def binary():
    cnt = 1 # 블루레이 개수
    sum = 0
    for i in length:
        sum += i
        if sum > mid:
            cnt += 1
            sum = i
    return cnt

while(left <= right):
    mid = (left + right) // 2
    # left 9, mid 17, right 26, cnt = 3
    cnt = binary()
    if cnt <= m: # 작으면 더 작게 나누어주어야 함
        right = mid - 1
    elif cnt > m: # 크면 큼직큼직하게 나누어주어야 함
        left = mid + 1

print(left) # ???ㅠㅠㅠ

