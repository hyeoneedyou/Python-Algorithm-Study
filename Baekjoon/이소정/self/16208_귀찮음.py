# 쇠막대의 수 : n
# 쇠막대의 길이 : a1, a2, ..., an

# 18점
# n = int(input())
# bar = list(map(int, input().split()))
# bar.sort()
# result = 0

# # 2 3 4 5
# for i in range(n): # 0
#   sum = 0
#   for j in range(i+1, n): # 1 2 3
#     sum += bar[j]
#   result += bar[i] * sum
# print(result)

# 30점
n = int(input())
bar = list(map(int, input().split()))

cost = 0 
sum = 0 
l = len(bar)

for i in bar:
  sum += i

for i in range(0, l-1):
  sum -= bar[i]
  cost += bar[i]*sum 

print (cost)