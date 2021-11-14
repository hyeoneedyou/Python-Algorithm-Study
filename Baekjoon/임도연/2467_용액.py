n = int(input())
array = list(map(int, input().split()))

right = n
left = -1
for i in range(n):
    if array[i] < 0:
        left += 1
    elif array[i] > 0:
        right -= 1

if right == n:
    print(array[left - 1], array[left])
elif left == -1:
    print(array[0], array[1])
else:
    result_value = [0, 0]
    result = 2000000000

    origin_left = left
    origin_right = right
    while True:
        if right == n or left == -1:
            break
        temp = array[left] + array[right]

        result = min(result, abs(temp))
        if result == abs(temp):
            result_value = [array[left], array[right]]

        if result == 0:
            break

        # -99 -2 -1 4 98
        if temp > 0:
            left -= 1
        elif temp < 0:
            right += 1

    if origin_left > 1:
        left_min = array[origin_left - 1] + array[origin_left]
        result = min(result, abs(left_min))
        if result == abs(left_min):
            result_value = [array[origin_left - 1], array[origin_left]]

    if origin_right < n - 2:
        right_min = array[origin_right] + array[origin_right + 1]
        result = min(result, abs(right_min))
        if result == abs(right_min):
            result_value = [array[origin_right], array[origin_right + 1]]

    print(" ".join(map(str, result_value)))
