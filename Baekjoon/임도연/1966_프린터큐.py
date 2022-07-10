t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))

    result = 0
    while True:
        current_doc = priority[0]

        if current_doc == max(priority):
            priority = priority[1:]
            result += 1
            if m == 0:
                break
        else:
            priority = priority[1:]
            priority.append(current_doc)

        m = m - 1 if m > 0 else len(priority) - 1

    print(result)
