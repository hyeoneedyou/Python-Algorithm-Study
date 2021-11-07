from collections import deque

n, k = map(int, input().split())
root = [0] * 1000001


def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(root[x])
            break
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i <= 1000000 and not root[i]:
                root[i] = root[x] + 1
                q.append(i)


bfs()
