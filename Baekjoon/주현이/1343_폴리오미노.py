a = input()

a = a.replace('XXXX', 'AAAA') # replace 사용
a = a.replace('XX', 'BB')

if 'X' in a:
    print(-1)
else:
    print(a)

