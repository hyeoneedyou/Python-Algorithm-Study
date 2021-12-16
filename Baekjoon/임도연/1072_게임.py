game, win = map(int, input().split())
z = (win * 100) // game

# 지금까지한 게임 횟수만큼을 다시 한다고 생각한다면
# win / game  <=  win + game  / 2game    win <= game

if z >= 99:
    print(-1)
    exit()

left = 1
right = game
answer = -1
while left <= right:
    mid = (left + right) // 2
    temp_mid = ((win + mid) * 100) // (game + mid)

    if temp_mid > z:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)