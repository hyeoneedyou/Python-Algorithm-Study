n = int(input())
mod = 10 ** 9

# 끝자리 숫자가 0~9일때 경우의 수를 계산
arr = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

for i in range(1, n):
    new_arr = []
    for j in range(10):
        if j == 0:
            new_arr.append(arr[i - 1][j + 1])
        elif j == 9:
            new_arr.append(arr[i - 1][j - 1])
        else:
            new_arr.append(arr[i - 1][j - 1] + arr[i - 1][j + 1])

    arr.append(new_arr)

print(sum(arr[n - 1]) % mod)