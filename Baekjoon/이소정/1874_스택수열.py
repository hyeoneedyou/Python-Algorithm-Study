# 4 3 6 8 7 5 2 1
# 1 2 3 4
# 1 2                    4 3
# 1 2 5 6
# 1 2 5                  4 3 6
# 1 2 5 7 8 
# 1 2 5                  4 3 6 8 7
#                        4 3 6 9 7 5 2 1

n = int(input())
stack = []
result = []
num = 0
isPossible = True

for i in range(n):
    value = int(input())
    while num < value:
      num += 1
      result.append("+")
      stack.append(num)

    if stack[-1] == value:
        stack.pop()
        result.append("-")
    else :
        isPossible = False
    
if isPossible == False:
    print("NO")
else :
  for i in result:
      print(i)
