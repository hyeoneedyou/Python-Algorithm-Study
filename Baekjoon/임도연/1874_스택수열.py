n = int(input())

numbers = [int(input()) for _ in range(n)]

stack = []

index = 0
num = 1

result = []
while num <= n:
    stack.append(num)
    result.append("+")
    while True:
        if len(stack) == 0:
            break
        if index >= n:
            break
        if stack[-1] != numbers[index]:
            break
        stack.pop(-1)
        result.append("-")
        index += 1
    num += 1

if len(stack) == 0:
    print("\n".join(result))
else:
    print("NO")
