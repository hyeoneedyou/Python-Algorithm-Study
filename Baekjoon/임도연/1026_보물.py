# 길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.
# S = A[0]×B[0] + ... + A[N-1]×B[N-1]
# S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.
# S의 최솟값을 출력하는 프로그램을 작성하시오.

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
copyB = list(b)
resultA = [0] * n
for i in range(n):
    b_idx = copyB.index(max(copyB)) # B 최댓값 위치
    resultA[b_idx] = a[i]
    copyB[b_idx] = -1

result = 0
for i in range(n):
    result += resultA[i] * b[i]
print(result)

