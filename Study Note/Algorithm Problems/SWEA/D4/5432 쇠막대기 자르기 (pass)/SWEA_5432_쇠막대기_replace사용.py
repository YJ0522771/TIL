import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////
    s = input()
    arr = s.replace('()', '|')

    index = 0
    count = 0
    for s in arr:
        if s == '(':
            index += 1
        elif s == ')':
            index -= 1
            count += 1
        else:
            count += index

    print('#{} {}'.format(test_case, count))
