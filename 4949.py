while True:
    temp = input()
    stack = []
    if temp == '.':
        break
    for i in temp:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                stack.append(i)
                break
            elif stack[-1] == '(':
                del stack[-1]
            else:
                stack.append(i)
                break
        elif i == ']':
            if len(stack) == 0:
                stack.append(i)
                break
            elif stack[-1] == '[':
                del stack[-1]
            else:
                stack.append(i)
                break
    if len(stack)==0:
        print('yes')
    else:
        print('no')