# 성공
s = input()


def is_check(s):  # 올바른 괄호열인지 확인하는 함수
    stack = []
    flag = True
    
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
        
        else:  # ) ]
            if s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    flag = False
            
            else:  # ]
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    flag = False
    
    if not stack and flag:
        return True
    return False


def calc_value(s):  # 괄호의 값을 계산하는 함수
    stack = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
        
        else:  # ) ]
            if s[i] == ')':
                if stack[-1] == '(':
                    stack[-1] = 2
                else:  # 올바른 괄호열이기 때문에 숫자만 있다.
                    temp = 0
                    for idx in range(len(stack) - 1, -1, -1):  # 괄호 만날 때까지 계속 더해주기 (XY) = X + Y
                        if stack[idx] == '(':
                            stack[-1] = temp * 2
                            break
                        else:  # ==> type(stack[idx]) == int
                            temp += stack[-1]
                            stack.pop()
            
            else:  # ]
                if stack[-1] == '[':
                    stack[-1] = 3
                else:  # 올바른 괄호열이기 때문에 숫자만 있다.
                    temp = 0
                    for idx in range(len(stack) - 1, -1, -1):  # 괄호 만날 때까지 계속 더해주기 (XY) = X + Y
                        if stack[idx] == '[':
                            stack[-1] = temp * 3
                            break
                        else:  # ==> type(stack[idx]) == int
                            temp += stack[-1]
                            stack.pop()
    return sum(stack)


if is_check(s):
    print(calc_value(s))
else:
    print(0)
# # 실패
# a = input()
# stack = []
# ans = 0
# flag = True
# c = []
# last = []
# status = None
# final = 0
# for i in range(len(a)):
#     t = a[i]
#     if t == '(' or t =='[':
#         stack.append(t)
#         status = 'append'
#     elif t == ')' or t == ']':
#         while stack:
#             p = stack.pop()
#
#             if t == ')' and p != '(':
#                 flag = False
#                 break
#             elif t == ']' and p!= '[':
#                 flag = False
#                 break
#             else:
#                 if not flag:
#                     break
#                 if t == ')' and p == '(':
#                     if status == 'pop':
#                         while c:
#                             tmp = c.pop()
#                             if len(stack) == 0:
#                                 ans += tmp
#                                 ans = ans * 2
#                                 last.append(ans)
#                                 ans = 0
#                                 status = None
#                             else:
#                                 ans += tmp * 2
#                     elif status == 'append':
#                         if len(stack) == 0:
#                             ans += 2
#                             last.append(ans)
#                             ans = 0
#                             status = None
#                         else:
#                             c.append(2)
#
#                 elif t == ']' and p == '[':
#                     if status == 'pop':
#                         while c:
#                             tmp = c.pop()
#                             if len(stack) == 0:
#                                 ans += tmp
#                                 ans = ans * 3
#                                 last.append(ans)
#                                 ans = 0
#                                 status = None
#                             else:
#                                 ans += tmp * 3
#                     elif status == 'append':
#                         if len(stack) == 0:
#                             ans += 3
#                             last.append(ans)
#                             ans = 0
#                             status = None
#                         else:
#                             c.append(3)
#         status = 'pop'
#
#
# if flag:
#     for j in range(len(last)):
#         final += last[j]
#     print(final)
# else:
#     print(0)