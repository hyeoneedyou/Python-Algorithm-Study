n = input()

result = 0
stack = []

# 올바르지 못한 입력
if n.count('(') != n.count(')') or n.count('[') != n.count(']'):
    print(0)
else:
    for c in n:
        temp = 1
        flag = False  # 안에 다른 종류의 괄호가 있는 경우를 체크
        if c == '(':
            stack.append(c)
        elif c == '[':
            stack.append(c)
        elif c == ')':
            while True:
                if stack.pop() == '(':
                    temp = 2
                    break
                elif stack.pop() == ']':
                    flag = True
                elif stack.pop() == '[':
                    temp = 3
                if flag:
                    result *= temp
                else:
                    result += temp
        elif c == ']':

    print(result)

# 닫는 괄호를 또 만나면 곱하기 아니면 더하기
