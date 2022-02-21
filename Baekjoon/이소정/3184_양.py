# 코드 수정하기 -> 에러있음

R, C = map(int,input().split())
pos = [list(input().rstrip()) for _ in range(R)]

visited = [[False] * C for _ in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
	sheep, wolf = 0, 0
	q = []
	q.append([x, y])
	while q:
		x = q[0][0]
    y = q[0][1]
		if pos[x][y] == 'o':
			sheep += 1
		if pos[x][y] == 'v':
			wolf += 1
		pos[x][y] = '#'
		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			if 0 <= nx < R and 0 <= ny < C and pos[nx][ny] != '#' and not visited[nx][ny]:
				visited[nx][ny] = True
				q.append([nx, ny])
	if sheep > wolf:
		wolf = 0
	else:
		sheep = 0
	return sheep, wolf

sheep_cnt, wolf_cnt = 0, 0
for i in range(R):
	for j in range(C):
		if pos[i][j] == 'o' or pos[i][j] == 'v':
			sheep, wolf = bfs(i, j)
			sheep_cnt += sheep
			wolf_cnt += wolf
print(sheep_cnt, wolf_cnt)