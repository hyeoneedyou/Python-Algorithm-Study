n = int(input())

array = [int(input()) for _ in range(n)]
array.sort()

result = 0
for i in range(1, n + 1):
    result += abs(array[i - 1] - i)

print(result)