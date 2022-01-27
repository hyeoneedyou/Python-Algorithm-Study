# n 강의 수, m 블루레이 개수
n, m = map(int, input().split())

# 강의 순서대로 크기
lecture_size = list(map(int, input().split()))

left = max(lecture_size)
right = sum(lecture_size)

while left <= right:
    mid = (left + right) // 2
    disk_count = 1
    temp = 0
    for lecture in lecture_size:
        temp += lecture
        if temp > mid:
            disk_count += 1
            temp = lecture
    if disk_count > m:
        left = mid + 1
    elif disk_count <= m:
        right = mid - 1

print(left)