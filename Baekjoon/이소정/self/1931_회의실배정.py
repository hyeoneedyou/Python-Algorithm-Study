# 한 개의 회의실 : N개의 회의
# 회의의 최대 개수

# 1 4
#     5 7
#         8 11 
#              12 14

N = int(input())
all = []

for _ in range(N):
  meeting = list(map(int, input().split()))
  all.append(meeting)
all = sorted(all, key=lambda single: single[0])
all = sorted(all, key=lambda single: single[1])
# print(all)  

count = 0
# start = 0
finish = 0 # [0, 0]
for arr in all:
  if arr[0] >= finish:
    # start = arr[0]
    finish = arr[1]
    count += 1
print(count)