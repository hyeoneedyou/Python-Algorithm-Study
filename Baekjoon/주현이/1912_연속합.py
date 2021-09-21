n = int(input())
nums = list(map(int, input().split()))
ans_list = []
for i in range(n):
    for j in range(i, n):
        ans_list.append(sum(nums[i:j+1]))
print(max(ans_list))
