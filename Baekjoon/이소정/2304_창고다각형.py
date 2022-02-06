n = int(input())

wall = [0] * 20
# 0 1 2 3 4 5 6 7 8  9 10 11 12 13 14 15 16
# 0 0 4 0 6 3 0 0 10 0 0  4  0  6  0  8  0
box = [0] * 20
# 0 0 
max_l = 0

for _ in range(n):
    l, h = map(int, input().split())
    max_l = max(l, max_l)
    wall[l] = h
    box[l] = h

for i in range(max_l+1): # 0~15
    # 다음 값이 나보다 작으면 내 값을 다음 값에 주기
    if wall[i] > wall[i+1]:
        box[i+1] = box[i]

print(wall)
print(box)