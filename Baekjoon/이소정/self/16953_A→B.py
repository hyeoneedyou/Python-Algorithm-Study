# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다.

A, B = map(int, input().split())

def bfs(A, B):
	# 준비
	q = [[A, 1]] # 현재
	# visited = [0] * (B+ 1); # 메모리 초과
	count = 0

	while q:
		# 1. 현재 선택
		now = q[0][0] # 지금
		count = q[0][1] # 지금 카운트
		# 2. 삭제하기
		del q[0]
		# 3. 방문했니?
		# if visited[now] == 0: # 안함
			# 3.1. 방문 처리한다.
			# visited[now] = 1
		# 3.2. 찾는 노드니?
		if now == B:
			return count
		# 3.3. 찾는 노드가 아니면 조건에 따라 q에 append한다.
		if (now * 2) <= B:
			q.append([now * 2, count + 1]) # 2배니까 다른 경우로 미리 방문될 수 없음
		if (int(str(now) + "1")) <= B: # 홀수니까 당연히 처음 방문한 곳
			q.append([int(str(now) + "1"), count + 1])
	return -1 # 모두 비었을 경우에는 -1

print(bfs(A, B))
