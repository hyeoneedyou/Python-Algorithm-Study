import math

n = int(input())
start = 0
end = n**(1/2)
target = n**(1/2)
result = 0

if type(target) == int:
    ans = target
else:
    ans = math.ceil(target)

print(ans)
