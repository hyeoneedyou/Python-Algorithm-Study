n = int(input())
boxes = list(map(int, input().split()))

result = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if boxes[j] < boxes[i]:
            result[i] = max(result[j] + 1, result[i])

print(max(result))