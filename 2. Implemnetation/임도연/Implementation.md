# 구현
> 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정
>
> ex) **완전탐색** : 모든 경우의 수를 주저 없이 다 계산하는 해결 방법
>
> ex) **시뮬레이션** : 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행해야 하는 문제 유형

## 메모리 제약 사항
- 파이썬 리스트 크기

## [문제] 상하좌우
> 여행가 A는 N * N 크기의 정사각형 공간 위에 서 있다.
> 이 공간은 1 * 1 크기의 정사각형으로 나누어져 있다.
> 가장 왼쪽 위 좌표는 (1, 1)이며 가장 오른쪽 아래 좌표는 (N, N,)이다.
> 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며 시작은 항상 (1, 1)이다.

-> 시뮬레이션 유형.
```python
# 교재 풀이
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
    
print(x, y)
```
```python
# 내 풀이
n = int(input())
plan = input().split()
dic = {'U':0, 'D':1, 'L':2, 'R':3}
x, y = 1, 1
# U, D, L, R 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(len(plan)):
    px = d[0] + dx[dic[plan[i]]]
    py = d[1] + dy[dic[plan[i]]]
    if px < 1 or px > n or py < 1 or py > n:
        continue
    x, y = px, py

print(x, y)
```

## [문제] 시각
> 정수 N이 입력되면 00시 00뷴 00초부터 N시 59분 59초까지의 모든 시각 중에서
> 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.

-> 완전탐색 유형.
```python
# 교재 풀이
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
```
```python
# 내 풀이
n = int(input())

result = (n + 1) * 60 * 60
if n > 2:
    result -= (n) * 45 * 45
elif n > 12:
    result -= (n - 1) * 45 * 45
elif n > 22:
    result -= (n - 2) * 45 * 45
else:
    result -= (n + 1) * 45 * 45

print(result)
```
## [문제] 왕실의 나이트
> 8 * 8 좌표평면의 특정 한 칸에 나이트가 서 있다.
> 나이트는 L자 형태로만 이동할 수 있으며 정원 밖으로 나갈 수 없다.
>  1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기.
>   2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기.
> 행은 1 ~ 8, 열은 a ~ h로 표현한다.

-> dx, dy 리스트 선언과 steps 두 가지 방식을 주로 사용.
```python
# 교재 풀이
input_data = input()
row = int(input_data[0])
column = int(input_data[1])

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
        
print(result)
```
```python
# 내 풀이
n = input()
r, c = int(n[1]), n[0]  # 현재 위치 행, 열

dx = [2, 2, -2, -2, 1, 1, -1, 1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

result = 0
for i in range(8):
    x = r + dx[i]
    y = ord(c) - ord('a') + dy[i]

    if x < 1 or x > 8 or y < 0 or y > 8:
        continue
    else:
        result += 1

print(result)
```

## [문제] 게임개발
> 캐릭터가 있는 장소는 1 * 1 크기의 정사각형으로 이뤄진 N * M 크기의 직사각형으로
> 각각의 칸은 육지 또는 바다이다.
> 캐릭터는 동서남북 중 한 곳을 바라본다.
> 각 칸은 (A, B)로 나타내며, A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수이다.
> 캐릭터는 상하좌우로 이동할 수 잇고, 바다에는 갈 수 없다.
>   1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
>   2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
>      왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 횐전만 수행하고 1단계로 돌아간다.
>   3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
>      단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
> 
> 위 매뉴얼을 따라 캐릭터를 이동시킨 뒤, 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.

-> 시뮬레이션 유형, 리스트 컴프리헨션 문법을 사용한 리스트 초기화.
```python
# 교재 풀이
n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
```
```python
# 내 풀이
n, m = map(int, input().split())
# d = 북동남서 (0123)
x, y, d = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 상우하좌 이동 (북동남서와 매칭)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 1
rotate = 0
array[x][y] = 2

while True:
    # 네 방향 다 가보거나 바다인 경우
    if rotate > 3:
        d = d + 2 if d < 2 else d - 2
        if array[x + dx[d]][y + dx[d]] == 1: # 뒤가 바다인 경우
            break
        else: # 뒤로 한 칸 이동
            x = x + dx[d]
            y = y + dy[d]
            rotate = 0
            continue
    d = d - 1 if d != 0 else 3 # 왼쪽으로 회전
    rotate += 1
    if array[x + dx[d]][y + dy[d]] == 0:
        array[x + dx[d]][y + dy[d]] = 2
        x = x + dx[d]
        y = x + dy[d]
        result += 1
        rotate = 0

print(result)
print(array)

```

