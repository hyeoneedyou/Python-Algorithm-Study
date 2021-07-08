# 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다.
# 숫자가 쓰인 카드들이 N * M 형태로 놓여 있다. 이때 N은 행의 개수, M은 열의 개수를 의미한다.
# 뽑을 카드의 행을 선택하고 그중 가장 숫자가 낮은 카드를 선택한다.
# 여러 경우의 수 중에서 가장 높은 숫자의 카드를 구하라.

n, m = map(int, input().split())

array = []
min_array = []
for i in range(n):
        array.append(list(map(int, input().split())))
        min_array.append(min(array[-1]))

print(max(min_array))


# # 교재 풀이 => 공간효율적
# n, m = map(int, input().split())
#
# result = 0
# for i in range(n):
#         data = list(map(int, input().split()))
#         min_value = min(data)
#         result = max(result, min_value)
#
# print(result)
