s = input()
n = []
for i in range(len(s)):
    n.append(int(s[i]))

ans = n[0]

for i in range(1, len(n)):
    ans = max(ans+n[i], ans*n[i])

print(ans)