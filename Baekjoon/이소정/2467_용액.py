# 왜 안되는지 도무지 모르겠다....
# N = int(input())
# liq = list(map(int, input().split()))
# l = 0
# r = N-1
# store = [abs(liq[l]+liq[r]), [liq[l],liq[r]]]

# while l<r:
#   sum = liq[l] + liq[r]
#   if abs(sum) < store[0]:
#     store[0] = abs(sum)
#     store[1] = [liq[l], liq[r]]
#   if sum < 0: # left 이동
#     l += 1
#   elif sum > 0: # right 이동
#     r -= 1
#   else: # sum이 0이면
#     print(*store[1])   
#     break
# print(*store[1])

def solution(liq):
    l=0
    r=len(liq)-1
    ans = [abs(liq[l]+liq[r]),[liq[l],liq[r]]]

    while l<r:
        mix = liq[l]+liq[r]
        if abs(mix) < ans[0]:
            ans[0] = abs(mix)
            ans[1] = [liq[l],liq[r]]
        if mix > 0:
            r-=1
        elif mix < 0:
            l += 1
        else:
            return ans[1]
    return ans[1]

n = map(int,input().split())
liq = list(map(int,input().split()))
ans = solution(liq)
print(*ans)
