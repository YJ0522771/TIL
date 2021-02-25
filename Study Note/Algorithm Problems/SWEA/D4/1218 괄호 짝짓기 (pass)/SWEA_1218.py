import sys
sys.stdin = open("input.txt", "r")

opens = ['(', '[', '{', '<']
closes = [')', ']', '}', '>']

T = 10
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ////////////////////////////////////////////////
    N = int(input())
    string = input()
    stack = []
    state = True
    for s in string:
        if s in opens:
            stack.append(s)
        else:
            if len(stack) and stack[len(stack) - 1] == opens[closes.index(s)]:
                stack.pop()
            else:
                state = False
                break

    print('#{} {}'.format(test_case, int(state)))

