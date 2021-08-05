import math

n = int(input())
target = n**(1/2)
result = 0

if type(target) == int:
    ans = target
else:
    ans = math.ceil(target)

print(ans)
