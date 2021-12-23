# 0 1 2 3 4 5 6 7
# 0 0 0 0 2 2 1 1

# 9 2
# ARR : 3 2 5 5 6 4 4 5 7
#             l
#                         R
# RESULT : 7

N, K = map(int, input().split())
arr = list(map(int, input().split()))

count = [0] * (max(arr) + 1)
result = 0
left = 0
right = 0

while right < len(arr):
    if count[arr[right]] < K: # K보다 작으면
        count[arr[right]] += 1
        right += 1

    else : # K보다 같거나 크면
        count[arr[left]] -= 1
        left += 1
    result = max(result, right - left)

print(result)