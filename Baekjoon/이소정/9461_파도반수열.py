T = int(input())
dp = [0] * 101 
dp[1], dp[2], dp[3]= 1, 1, 1

def solution(N):
    for j in range(1, N-2):
        dp[j+3] = dp[j]+dp[j+1]
    return dp[N]

# input을 받을 때마다 solution 함수를 돌리기 때문에 비효율적이다.
# input을 리스트로 받고, max만큼 dp 생성한다.
for i in range(T):
    N = int(input())
    print(solution(N))
