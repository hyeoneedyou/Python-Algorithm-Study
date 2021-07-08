# 이 문제의 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
# 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.
# 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다.
# 이벽값으로 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 큰 수의 법칙에 따른 결과를 출력하시오.

n, m, k = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
f = array[-1]  # 가장 큰 수
s = array[-2]  # 두번째로 큰 수

result = f * (m // k) * k + s * (m % k)

print(result)


# 교재 풀이
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
# data.sort()
# first = data[n - 1]  # 가장 큰 수
# second = data[n - 2]  # 두 번째로 큰 수
#
# count = int(m / (k + 1)) * k
# count += m & (k + 1)
#
# result = 0
# result = count * first
# result += (m - count) * second
#
# print(result)
