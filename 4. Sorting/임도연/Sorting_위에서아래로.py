# 수가 크기에 상관없이 나열되어 있다.
# 내림차순으로 정렬하는 프로그램을 만드시오.

n = int(input())

array = [0] * n
for i in range(n):
    array[i] = int(input())

array.sort(reverse=True)

for data in array:
    print(data, end=' ')