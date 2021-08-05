n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 1
end = max(array)

# result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    # for x in array:
    #     if x > mid:
    #         total += x - mid
    total = sum([x - mid if (x - mid) > 0 else 0 for x in array])
    if total < m:
        end = mid - 1
    else:
        # result = mid    # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

print(end)
# print(result)
