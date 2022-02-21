# 0  1  2   3  4
# 50 10 100 20 40
# 30 50 70 10 60

# 0  1         2        3       4
# 50 10+30=40  100->200 20->140 40->250
# 30 50+50=100 70->120  10->210 60->260


t = int(input())
for _ in range(t):
    arr = []
    # 몇 열?
    n = int(input())
    for i in range(2):
        arr.append(list(map(int, input().split())))
    for j in range(1, n): # 1열부터 n-1열까지
        if j == 1:
            arr[0][j] += arr[1][j-1] # 50 + 50
            arr[1][j] += arr[0][j-1] # 10 + 30
        else:
            arr[0][j] += max(arr[1][j-1], arr[1][j-2])
            arr[1][j] += max(arr[0][j-1], arr[0][j-2])
    print(max(arr[0][n-1], arr[1][n-1]))