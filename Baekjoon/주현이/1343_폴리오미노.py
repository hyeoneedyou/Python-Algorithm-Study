a = input().split('.')
p = True

for i in range(len(a)):
    if len(a[i]) == 4:
        a[i] = 'AAAA'

    elif len(a[i]) == 2:
        a[i] = 'BB'

    elif len(a[i]) % 4 == 0:
        a[i] = 'AAAA'* (len(a[i]) // 4)

    elif len(a[i]) % 4 == 2:
        a[i] = 'AAAA'* (len(a[i]) // 4) + 'BB'

    else:
        p = False   

if p == False:
    print(-1)

else:    
    for i in range(len(a)):  
        if len(a[i]) != 0:
            if i == len(a)-1:
                print(a[i])
            else:
                print(a[i], end='.')
        else:
            print('.', end='')