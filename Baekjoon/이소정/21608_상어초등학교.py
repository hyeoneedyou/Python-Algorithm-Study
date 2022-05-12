n = int(input())
students = []
table = [[0 for _ in range(n)] for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n*n):
		students.append(list(map(int, input().split())))
		like = 0
		empty = 0
		temp = []
		for i in range(n):
				for j in range(n):
						if table[i][j] == 0:
								empty_cnt = 0
								like_cnt = 0
								for k in range(4):
										nx = i + dx[k]
										ny = j + dy[k]
										if (0 <= nx and nx < n) and (0 <= ny and ny < n):
												if table[nx][ny] == 0:
														empty_cnt += 1
												if table[nx][ny] in students[-1]:
														like_cnt += 1
								temp.append([like_cnt, empty_cnt, i, j])
		temp.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
		table[temp[0][2]][temp[0][3]] = students[-1][0]

result = 0
students.sort()
for i in range(n):
		for j in range(n):
				score = 0
				for k in range(4):
						nx = i + dx[k]
						ny = j + dy[k]
						if (0 <= nx and nx < n) and (0 <= ny and ny < n):
								if table[nx][ny] in students[table[i][j]-1]:
										score += 1
				if score != 0:
						result += 10 ** (score-1)
print(result)