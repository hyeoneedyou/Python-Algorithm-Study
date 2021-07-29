n, m = map(int, input().split())
array = list(map(int, input().split()))

maxH = max(array)

start = 0
end = maxH

result = 0
while start <= end:
    mid = (start + end) // 2
    sum_array = 0
    for wood in array:
        if wood > mid:
            sum_array += wood - mid
    if sum_array >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
