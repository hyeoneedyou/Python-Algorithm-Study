n = int(input())
s = list(map(int, input().split()))
tmp = 0
ans = 1e9
a = 0
b = 0

for i in range(n//2 + 1):
    if n % 2 == 0:  # n이 짝수일 때
        if i == n//2:
            continue
        tmp = s[i] + s[-(i+1)]

        if abs(tmp) < ans:
            ans = tmp
            a = s[i]
            b = s[-(i + 1)]
    else:  # n이 홀수일 때
        if i == n//2:  # 중간일 때
            tmp = min(abs(s[i]+s[i-1]), abs(s[i]+s[i+1]))
            if abs(tmp) < ans:
                ans = tmp
                if tmp == abs(s[i]+s[i-1]):
                    a = s[i-1]
                    b = s[i]
                else:
                    a = s[i]
                    b = s[i+1]
        else:
            tmp = s[i] + s[-(i + 1)]
            if abs(tmp) < ans:
                ans = tmp
                a = s[i]
                b = s[-(i + 1)]
   

print(a, b)