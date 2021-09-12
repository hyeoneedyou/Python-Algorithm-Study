n = int(input())
a = []
a = list(map(int, input().split()))
print(a)
cnt = 1
# present = a[0]
# for i in range(n-1):
#     if present < a[i+1]:
#         cnt += 1
#         present = a[i+1]

present = min(a)
idx = a.index(present)
a.remove(present)
print(idx)