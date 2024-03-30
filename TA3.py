s = str(input())
operand = ['+', '-', '*', '/', '(', ')']
def validateNumber(s):
    for i in operand:
        s = s.replace(i, '')
    if len(s) == 0:
        return False
    for i in s.split():
        if i.isdigit():
            try:
                int(i)
                if int(i) > 255 or int(i) < 0:
                    return False
            except:
                return False
        else:
            return False
    return True
def tryToOpz(s):
    stack = []
    out = ""
    for i in s.split():
        if i.isdigit():
            out += i + ' '
        if i in operand:
            if len(stack) == 0:
                stack.append(i)
            elif i in ['*','/']:
                stack.append(i)
            elif i in ['+','-'] and stack[-1] in ['*','/']:
                while len(stack) > 0 and stack[-1] != '(':
                    out += stack[-1] + ' '
                    stack.pop()
            elif i == '(':
                stack.append(i)
            elif i == ')':
                while len(stack) > 0 and stack[-1] != '(':
                    out += stack[-1] + ' '
                    stack.pop()
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(i)
    while len(stack) > 0:
        out += stack[-1] + ' '
        stack.pop()
    return out
def calc(opz):
    stack = []
    for i in opz.split():
        if i.isdigit():
            stack.append(i)
        if i in operand:
            tmp = eval(str(str(stack[-2]) + i + str(stack[-1])))
            stack.pop()
            stack.pop()
            stack.append(tmp)
    return stack[-1]
def validate(s):
    if s.count(operand[4]) != s.count(operand[5]):
        print("Не достаточно скобок")
        return False
    if not validateNumber(s):
        print("Числовая ошибка")
        return False
    opz = tryToOpz(s)
    ans = calc(opz)
    if ans > 255 or ans < 0:
        print("Выход за границы")
    else:
        print(ans)

validate(s)