# 두 좌표 사이의 거리; 맨해튼 거리
def get_distance(from_position, to_position):
    return abs(from_position[0] - to_position[0]) + abs(from_position[1] - to_position[1])


def go(xy):
    if xy[0] == festival[0] and xy[1] == festival[1]:
        print("happy")
        return
    for i in range(n + 1):
        if get_distance(xy, destination[i]) <= 1000:
            go(destination[i])
    print("sad")


t = int(input())  # 테스트 케이스 개수

for _ in range(t):
    n = int(input())  # 편의점 개수
    house = list(map(int, input().split()))  # 집 좌표
    store = [list(map(int, input().split())) for _ in range(n)]  # 편의점 좌표
    festival = list(map(int, input().split()))  # 페스티벌 좌표

    destination = store
    destination.append(festival)
    road = [0 * (n + 2)]
    go(house)
