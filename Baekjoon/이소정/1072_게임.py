# X : 게임횟수
# Y : 이긴 게임
# F = X - Y : 진 게임

X, Y = map(int, input().split())
origin_Z = (Y * 100) // X # 원래 승률

left = 1
right = X

result = -1

if origin_Z >= 99:
    print(-1)
else:
    while (left <= right) : # 등호 조심!!
        mid = (left + right) // 2
        new_Z = ((Y + mid) * 100) // (X + mid)

        if origin_Z >= new_Z:
            left = mid + 1
        else :
            right = mid -1
            result = mid
    print(result)