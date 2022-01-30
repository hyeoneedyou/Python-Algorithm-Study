# 노드들 간의 거리가 1000m 이상이면 안됨
# 집 - 편의점1
#    - 편의점2
#    - 페스티벌 -> return

# x, y 좌표에서 ~ 다른 좌표까지의 거리
def bfs():
    visited = []
    q = [[home_x, home_y]]
    while q:
        now = q[0]
        now_x = now[0] # 지금 node
        now_y = now[1]
        del q[0] # 방문 node 삭제
        if now not in visited:
            visited.append(now)
            if abs(now_x - fest_x) + abs(now_y - fest_y) <= 1000:
                print("happy")
                return
            for i in range(n):
                if abs(now_x - conv[i][0]) + abs(now_y - conv[i][1]) <= 1000:
                    q.append([conv[i][0], conv[i][1]])            
    print("sad")
    return

t = int(input())
for _ in range(t):
    n = int(input()) # 편의점 개수
    # 집
    home_x, home_y = map(int, input().split())
    conv = []
    # 편의점
    for _ in range(n):
        x, y = map(int, input().split())
        conv.append([x, y])
    # 페스티벌
    fest_x, fest_y = map(int, input().split())
    bfs()
