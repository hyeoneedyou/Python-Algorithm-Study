# 정수 N이 입력되면 00시 00뷴 00초부터 N시 59분 59초까지의 모든 시각 중에서
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.

n = int(input())

result = (n + 1) * 60 * 60
if n > 2:
    result -= (n) * 45 * 45
elif n > 12:
    result -= (n - 1) * 45 * 45
elif n > 22:
    result -= (n - 2) * 45 * 45
else:
    result -= (n + 1) * 45 * 45

print(result)

# # 교재 풀이
# h = int(input())
#
# count = 0
# for i in range(h + 1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 count += 1
#
# print(count)