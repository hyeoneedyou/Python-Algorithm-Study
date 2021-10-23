n = int(input())
p = list(map(int, input().split()))
ans = []
p.sort(reverse=True)
print(p)

i = 0
while True:
    if i+p[i] > len(p):
        break
    tmp = []
    for j in range(i, i+p[i]):
        if i + p[i] > len(p):
            break
        tmp.append(p[j])
    i = j
    ans.append(tmp)
        
print(len(ans))

print(ans)
# 5
# 2 3 1 2 2
