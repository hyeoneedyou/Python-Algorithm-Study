a = input()
stack = []
ans = 0
flag = True
c = []
status = None
for i in range(len(a)):
    t = a[i]
    if t == '(' or t =='[':
        stack.append(t)
        status = 'append'
    elif t == ')' or t == ']':
        p = stack.pop()

        if t == ')' and p != '(':
            flag = False
        elif t == ']' and p!= '[':
            flag = False
        else:
            if t == ')' and p == '(':
                if status == 'pop':
                    tmp = c.pop()
                    ans += tmp * 2
                elif status == 'append':
                    c.append(2)
                elif len(stack) == 0:
                    ans += c.pop()
                    status = None
            if t == ']' and p == '[':
                if status == 'pop':
                    tmp = c.pop()
                    ans += tmp * 3
                elif status == 'append':
                    c.append(3)
                elif len(stack) == 0:
                    ans += c.pop()
                    status = None
        status = 'pop'
        
if flag:
    print(ans)
else:
    print(0)