# 5 17
# 위치가 x라면
# 양 옆
# 2*x

N, K = map(int, input().split())

def bfs(N, K):
	count = 0
	q = [[N, 0]] # node, count
	visited = [0] * 100001 # 런타임에러 원인..!! 100000아니고 100001 해줘야 한다.

	while q:
		now = q[0][0] # 지금 node
		count = q[0][1]
		del q[0] # 방문 node 삭제
		# 방문 했는지 확인
		if visited[now] == 0:
			visited[now] = 1 # 방문 node => 1 처리
			if now == K:
				return count
			# 가지 만들기
			if (now * 2) <= 100000:
				q.append([now*2, count+1])
			if (now + 1) <= 100000:
				q.append([now+1, count+1])
			if (now - 1) >= 0:
				q.append([now-1, count+1])
	return count

print(bfs(N, K))

