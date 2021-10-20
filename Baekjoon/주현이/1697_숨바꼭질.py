from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001


def bfs(n, k):
    q = deque()
    q.append([n, 0])  # node, count
    while q:
        x = q.popleft()
        now = x[0]
        cnt = x[1]
        # 처음 방문했을 때만 append 해줘야 최소
        if visited[now] == 0:
            visited[now] = 1
            if now == k:
                break
            if (now * 2) <= 100000:
                q.append([now * 2, cnt + 1])
            if (now + 1) <= 100000:
                q.append([now + 1, cnt + 1])
            if (now - 1) >= 0:
                q.append([now - 1, cnt + 1])
        
    return cnt


print(bfs(n, k))
