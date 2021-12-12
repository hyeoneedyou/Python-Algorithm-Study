n = int(input())
trees = list(map(int, input().split()))

div_2 = 0 # 2로 나눴을 때 몫들
remain_2 = 0 # 2로 나눴을 때 나머지들
for tree in trees:
    div_2 += tree // 2
    remain_2 += tree % 2

if (div_2 - remain_2) % 3 == 0 and div_2 >= remain_2:
    print("YES")
else:
    print("NO")