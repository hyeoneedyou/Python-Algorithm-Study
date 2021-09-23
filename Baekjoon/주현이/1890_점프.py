n = int(input())
board = [[0] * n for _ in range(n)]
res = []

for i in range(n):
    num = list(map(int, input().split()))
    for j in range(n):
        board[i][j] = num[j]

print(board)


def jump_down(x, y):
    p = False
    flag = True
    jump = board[x][y]
    if y+jump < n:
        if board[x][y+jump] == 0:
            flag = False
            return flag, p

        else:
            p = True
            return flag, p
    else:
        return flag, p


def jump_right(x, y):
    p = False
    flag = True
    jump = board[x][y]
    if x+jump < n:
        if board[x+jump][y] == 0:
            flag = False
            return flag, p

        else:
            p = True
            return flag, p
    else:
        return flag, p
   
d_next, d_p  = jump_down(0, 0)
r_next, r_p  = jump_right(0, 0)

# while d_next or r_next: