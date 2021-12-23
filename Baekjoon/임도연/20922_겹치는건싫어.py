n, k = map(int, input().split())
array = list(map(int, input().split()))

count = [0] * (max(array) + 1)
left = 0
right = 0
result = 0

while right < n:
    if count[array[right]] >= k:
        count[array[left]] -= 1
        left += 1
    else:
        count[array[right]] += 1
        right += 1
        result = max(result, right - left)

print(result)