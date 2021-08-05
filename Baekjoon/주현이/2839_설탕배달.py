m = int(input())
d = [5001] * (m+1)

array = [3, 5]
d[0] = 0
for i in range(len(array)):
    for j in range(array[i], m+1):
        if d[j - array[i]] != 5001:
            d[j] = min(d[j], d[j - array[i]] + 1)
            
if d[m] == 5001:
    print(-1)
else:
    print(d[m])
