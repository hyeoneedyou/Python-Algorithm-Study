N, M = input().split() 
N = int(N)
M = int(M)

result = 0

for i in range(N) :
  row= map(int, input().split())
  min_elt = min(row)
  result = max(min_elt, result)

print(result)
