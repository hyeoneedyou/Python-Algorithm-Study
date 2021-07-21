# 8 * 8 좌표평면의 특정 한 칸에 나이트가 서 있다.
# 나이트는 L자 형태로만 이동할 수 있으며 정원 밖으로 나갈 수 없다.
#   1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기.
#   2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기.
# 행은 1 ~ 8, 열은 a ~ h로 표현한다.

n = input()
r, c = int(n[1]), n[0]  # 현재 위치 행, 열

dx = [2, 2, -2, -2, 1, 1, -1, 1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

result = 0
for i in range(8):
    x = r + dx[i]
    y = ord(c) - ord('a') + dy[i]

    if x < 1 or x > 8 or y < 0 or y > 8:
        continue
    else:
        result += 1

print(result)

# # 교재 풀이
# input_data = input()
# row = int(input_data[0])
# column = int(input_data[1])
#
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
#
# result = 0
# for step in steps:
#     next_row = row + step[0]
#     next_column = column + step[1]
#     if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
#         result += 1
#
# print(result)
