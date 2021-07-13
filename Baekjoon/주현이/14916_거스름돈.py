n = int(input())
cnt = 0
back_count = 0

max_5 = n // 5

n %= 5

if (n % 2) == 0:
    cnt += max_5
else:
    for i in range(1, max_5+1):
        n += 5
        cnt = max_5 - i
        if (n % 2) ==0:
            break    
        
if (n % 2) == 0:
    cnt += n // 2
    print(cnt)
else:
    print(-1)