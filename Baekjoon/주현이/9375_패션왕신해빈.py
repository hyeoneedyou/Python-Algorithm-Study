a = int(input())
ans_list = []
for _ in range(a):
    b = int(input())
    dict = {}
    ans = 1
    for _ in range(b):
        n, m = input().split()
        if dict.get(m) is None:
            dict[m] = [n]
        else:
            dict.get(m).append(n)
    for key in dict.keys():
        ans *= len(dict[key]) + 1
    ans_list.append(ans-1)

for i in range(len(ans_list)):
    print(ans_list[i])