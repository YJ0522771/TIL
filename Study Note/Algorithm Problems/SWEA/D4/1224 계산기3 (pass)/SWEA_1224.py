import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # //////////////////////////////////////////////////
    N = int(input())
    in_str = input()
    post = ''
    stack = []
    for s in in_str:
        if s == '+':
            if len(stack) and stack[len(stack) - 1] == '*':
                while True:
                    post += stack.pop()
                    if (not len(stack)) or stack[len(stack) - 1] == '+' or stack[len(stack) - 1] == '(':
                        break
            stack.append(s)
        elif s == '*' or s == '(':
            stack.append(s)
        elif s == ')':
            while True:
                if not len(stack):
                    break
                temp = stack.pop()
                if temp == '(':
                    break
                else:
                    post += temp
        else:
            post += s

    while len(stack):
        post += stack.pop()

    # print(post)

    for p in post:
        if p == '*':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(a * b)
        elif p == '+':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(a + b)
        else:
            stack.append(p)
    print('#{} {}'.format(test_case, stack.pop()))