# A, B 두 배열은 N개의 원소로 구성되어 있으며 모두 자연수이다.
# 최대 K번의 바궈치기 연산을 수행할 수 있다.
# A의 모든 원소 합이 최대가 되도록하는 프로그램을 작성하시오.

n, k = map(int, input().split())
arrayA = sorted(list(map(int, input().split())))
arrayB = sorted(list(map(int, input().split())), reverse=True)

12345
54432
for i in range(k):
    if arrayA[i] >= arrayB[i]: break
    arrayA[i], arrayB[i] = arrayB[i], arrayA[i]

print(sum(arrayA))