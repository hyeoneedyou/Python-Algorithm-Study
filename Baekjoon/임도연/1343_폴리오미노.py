# 민식이는 다음과 같은 폴리오미노 2개를 무한개만큼 가지고 있다. AAAA와 BB
# 이제 '.'와 'X'로 이루어진 보드판이 주어졌을 때, 민식이는 겹침없이 'X'를 모두 폴리오미노로 덮으려고 한다.
# 이때, '.'는 폴리오미노로 덮으면 안 된다.
# 폴리오미노로 모두 덮은 보드판을 출력하는 프로그램을 작성하시오.

s = input()
board = [1]
cnt = 0
for i in range(1, len(s)): # x와 .의 개수를 리스트에 담기
    if s[i] != s[i - 1]:
        board.append(1)
    else:
        board[len(board) - 1] += 1

result = ''
flag = True if s[0] == '.' else False  # 시작이 X인 경우 0, .인 경우 1
for b in board:
    if flag:  # .일때
        result += '.' * b
        flag = False
    else:  # X일때
        if b % 2 != 0:  # 못 덮는 경우
            result = '-1'
            break
        else:
            a_board = b // 4
            b_board = (b % 4) // 2
            result += 'AAAA' * a_board + 'BB' * b_board
        flag = True

print(result)
