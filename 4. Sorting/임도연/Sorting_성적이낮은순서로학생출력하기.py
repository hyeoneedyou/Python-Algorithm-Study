# N명의 학생 정보는 이름과 성적으로 구분된다.
# 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.

n = int(input())
array = []
for i in range(n):
    name, score = input().split()
    array.append([name, int(score)])

array = sorted(array, key=lambda k:k[1])

for data in array:
    print(data[0], end=' ')