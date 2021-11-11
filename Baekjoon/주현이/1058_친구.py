n = int(input())

a = [ [] for _ in range(n)]

ans = []

for i in range(n):
    s = input()
    for j in range(len(s)):
        if s[j] == 'Y':
            a[i].append(1)
        else:
            a[i].append(0)
            

for i in range(n):
    ans.append(a[i].count(1))
    
print(a)
for i in range(n):
    for j in range(len(s)):
        if a[i][j] == 1:
            for k in range(i+1, n):
                if a[k][j] == 1:
                    ans[i] += 1
                    ans[j] += 1
print(max(ans))
