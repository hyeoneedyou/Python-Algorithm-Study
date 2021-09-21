n = int(input())
f = []
def get_lcm(a, b):
    lcm = 0
    a_aliquot = []
    b_aliquot = []
    
    for i in range(1, a+1):
        if a % i == 0:
            a_aliquot.append(i)
    for i in range(1, b+1):
        if b % i == 0:
            b_aliquot.append(i)
    aliquot = list(set(a_aliquot).intersection(b_aliquot))
    
    if len(aliquot) != 0:
        max_aliquot = max(aliquot)
        lcm = max_aliquot * (a//max_aliquot) * (b//max_aliquot)
    else:
        lcm = a * b
        
    return lcm


for i in range(n):
    ans = 0
    n1, n2 = map(int, input().split())
    ans = get_lcm(n1, n2)
    f.append(ans)
    
for i in range(len(f)):
    print(f[i])
    