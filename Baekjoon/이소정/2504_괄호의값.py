# ()  2
# []  3
# (x)  2*x
# [x]  3*x
# xy  x+y

# stack...? -> [] or ()

# 방법 1------------------------------------------
stack = []
s = list(input())

# stack : 
for i in s:
  if i == ")": # 2. ) ] 가 나오면 이전 것을 확인한다.
    temp = 0
    while stack: # 아무 것도 없을 때 까지
      top = stack.pop() # pop
      if top == "(":
        if temp == 0:
          stack.append(2)
        else:
          stack.append(2 * temp)
        break
      elif top == "[":
        print(0)
        exit() # 코드종료
      else : # 숫자인 경우
        temp += int(top)
      
  elif i == "]":
    temp = 0
    while stack: # 아무 것도 없을 때 까지
      top = stack.pop() # pop
      if top == "[":
        if temp == 0:
          stack.append(3)
        else:
          stack.append(3 * temp)
        break
      elif top == "(":
        print(0)
        exit()
      else : # 숫자인 경우
        temp += int(top)

  else: # 1. ( [ 이 나오면 stack에 넣는다.
    stack.append(i)

count = 0
for i in stack:
  if i == "(" or i == "[":
    print(0)
    exit()
  else :
    count += i

print(count)


# 방법 2------------------------------------------
# stack = []
# isPossible = input()
# s = list(isPossible)

# while True:
#   isPossible = isPossible.replace("()","")
#   isPossible = isPossible.replace("[]","")
#   if "()" not in isPossible and "[]" not in isPossible:
#     break;
# if isPossible != "":
#   print(0)
#   exit()
# else:
#   # stack : 
#   for i in s:
#     if i == ")": # 2. ) ] 가 나오면 이전 것을 확인한다.
#       temp = 0
#       while stack: # 아무 것도 없을 때 까지
#         top = stack.pop() # pop
#         if top == "(":
#           if temp == 0:
#             stack.append(2)
#           else:
#             stack.append(2 * temp)
#           break
#         else : # 숫자인 경우
#           temp += int(top)
        
#     elif i == "]":
#       temp = 0
#       while stack: # 아무 것도 없을 때 까지
#         top = stack.pop() # pop
#         if top == "[":
#           if temp == 0:
#             stack.append(3)
#           else:
#             stack.append(3 * temp)
#           break
#         else : # 숫자인 경우
#           temp += int(top)

#     else: # 1. ( [ 이 나오면 stack에 넣는다.
#       stack.append(i)

# count = 0
# for i in stack:
#   count += i

# print(count)