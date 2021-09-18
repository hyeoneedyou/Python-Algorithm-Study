def solution(n):
    stack = []
    result = 0
    for c in n:
        temp = 0
        if c == ')':
            while len(stack) != 0:
                top = stack.pop()
                if top == '(':
                    if temp == 0:
                        stack.append(2)
                    else:
                        stack.append(2 * temp)
                    break
                elif top == '[':
                    return 0
                else:
                    temp += int(top)
        elif c == ']':
            while len(stack) != 0:
                top = stack.pop()
                if top == '[':
                    if temp == 0:
                        stack.append(3)
                    else:
                        stack.append(3 * temp)
                    break
                elif top == '(':
                    return 0
                else:
                    temp += int(top)
        else:
            stack.append(c)

    for s in stack:
        if s == '(' or s == '[':
            return 0
        else:
            result += s
    return result

print(solution(list(input())))
