str = input()

result = []
for i in range(len(str)):
    result.append(str[i:])

result.sort()
print("\n".join(result))